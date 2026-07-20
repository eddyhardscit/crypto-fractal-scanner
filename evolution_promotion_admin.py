#!/usr/bin/env python3
"""Block 7 explicit Paper promotion administration.

Commands: list, approve, execute, rollback.
No command touches live trading or sends orders.
"""
from __future__ import annotations
import argparse, copy, csv, fcntl, hashlib, json, os, shutil, tempfile, uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from evolution_core import StrategyLifecycleManager, StrategyRegistry, StrategyStatus

CONTROL=Path('/root/crypto-fractal-scanner')
RUNTIME=Path('/opt/crypto-fractal-scanner-vps')
REPORTS=RUNTIME/'reports'
PLANS_PATH=REPORTS/'paper_trading_evolution_promotion_plans.json'
PROMOTION_STATE_PATH=REPORTS/'paper_trading_evolution_promotion_state.json'
CANDIDATE_STATE_PATH=REPORTS/'paper_trading_evolution_candidate_state.json'
CANDIDATE_REGISTRY_PATH=REPORTS/'paper_trading_evolution_candidate_registry.json'
REVIEW_PATH=REPORTS/'paper_trading_evolution_promotion_review.json'
PAPER_STATE_PATH=REPORTS/'paper_trading_state.json'
EVENTS_PATH=REPORTS/'paper_trading_evolution_promotion_events.csv'
CONFIG_PATH=RUNTIME/'config/evolution_promotion_block7.json'
APPROVAL_DIR=CONTROL/'data/evolution/promotion_approvals'
TRANSACTION_DIR=CONTROL/'data/evolution/promotion_transactions'
BACKUP_DIR=CONTROL/'data/evolution/backups'
LOCK_PATH=CONTROL/'data/evolution/promotion_admin.lock'
REGISTRY_PATH=CONTROL/'data/evolution/strategy_registry.json'
HISTORY_PATH=CONTROL/'data/evolution/evolution_history.json'

EVENT_FIELDS=['generated_utc','event_type','plan_id','candidate_id','candidate_portfolio','parent_id','parent_portfolio','family_id','old_status','new_status','review_hash','transaction_id','approved_by','reason']

def now(): return datetime.now(timezone.utc)
def iso(v=None): return (v or now()).astimezone(timezone.utc).isoformat(timespec='seconds')
def read(path,default):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError): return copy.deepcopy(default)
def atomic(path,value):
    path.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix='.'+path.name+'.',suffix='.tmp',dir=str(path.parent),text=True)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as h: json.dump(value,h,indent=2,sort_keys=True,ensure_ascii=False); h.write('\n'); h.flush(); os.fsync(h.fileno())
        os.replace(tmp,path)
    except Exception:
        try: os.unlink(tmp)
        except OSError: pass
        raise

def append_event(row):
    EVENTS_PATH.parent.mkdir(parents=True,exist_ok=True); exists=EVENTS_PATH.exists() and EVENTS_PATH.stat().st_size>0
    with EVENTS_PATH.open('a',encoding='utf-8',newline='') as h:
        w=csv.DictWriter(h,fieldnames=EVENT_FIELDS,extrasaction='ignore');
        if not exists: w.writeheader()
        w.writerow({k:row.get(k,'') for k in EVENT_FIELDS})

def stable_hash(v): return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':'),default=str).encode()).hexdigest()
def review_hash(row): return stable_hash({k:v for k,v in row.items() if k not in {'generated_utc','decision_summary'}})
def config(): return read(CONFIG_PATH,{})
def plans_doc(): return read(PLANS_PATH,{'plans':[]})
def find_plan(pid):
    doc=plans_doc()
    for p in doc.get('plans',[]):
        if p.get('plan_id')==pid: return doc,p
    raise RuntimeError(f'Unknown plan: {pid}')
def current_review(cid):
    doc=read(REVIEW_PATH,{'candidates':[]})
    for row in doc.get('candidates',[]):
        if row.get('candidate_id')==cid and row.get('status')=='PROMOTION_REVIEW_READY': return row
    raise RuntimeError('Candidate is no longer PROMOTION_REVIEW_READY')
def verify_fresh(plan):
    digest=review_hash(current_review(plan['candidate_id']))
    if digest!=plan.get('review_hash'): raise RuntimeError('Promotion plan is stale: review hash changed')
def open_count(name):
    state=read(PAPER_STATE_PATH,{'portfolios':{}}); p=state.get('portfolios',{}).get(name,{})
    return len(p.get('open_positions',[]) or [])
def save_plans(doc):
    doc['generated_utc']=iso(); atomic(PLANS_PATH,doc)
def approval_path(aid): return APPROVAL_DIR/(aid+'.json')
def transaction_path(tid): return TRANSACTION_DIR/(tid+'.json')
def registry(): return StrategyRegistry(REGISTRY_PATH,HISTORY_PATH)

def list_plans():
    rows=plans_doc().get('plans',[])
    return [{'plan_id':p.get('plan_id'),'status':p.get('status'),'candidate':p.get('candidate_portfolio'),'parent':p.get('parent_portfolio'),'review_hash':p.get('review_hash')} for p in rows]

def approve(plan_id,approved_by,confirmation,when=None):
    current=when or now(); doc,plan=find_plan(plan_id); verify_fresh(plan)
    if plan.get('status') not in {'PENDING_APPROVAL','APPROVED'}: raise RuntimeError(f"Plan cannot be approved from {plan.get('status')}")
    if confirmation!=plan.get('approval_confirmation'): raise RuntimeError('Exact approval confirmation does not match')
    cfg=config(); expires=current+timedelta(hours=int(cfg.get('approval_ttl_hours',72)))
    aid='APR-'+uuid.uuid4().hex[:20].upper()
    approval={'schema_version':1,'approval_id':aid,'plan_id':plan_id,'candidate_id':plan['candidate_id'],'parent_id':plan['parent_id'],'review_hash':plan['review_hash'],'approved_by':approved_by,'approved_utc':iso(current),'expires_utc':iso(expires),'status':'APPROVED','paper_only':True,'live_modified':False,'orders_sent':False}
    atomic(approval_path(aid),approval); plan.update({'status':'APPROVED','approval_id':aid,'approved_by':approved_by,'approved_utc':iso(current),'approval_expires_utc':iso(expires),'updated_utc':iso(current)}); save_plans(doc)
    append_event({'generated_utc':iso(current),'event_type':'PROMOTION_APPROVED','plan_id':plan_id,'candidate_id':plan['candidate_id'],'candidate_portfolio':plan['candidate_portfolio'],'parent_id':plan['parent_id'],'parent_portfolio':plan['parent_portfolio'],'family_id':plan['family_id'],'old_status':'PENDING_APPROVAL','new_status':'APPROVED','review_hash':plan['review_hash'],'approved_by':approved_by,'reason':'Explicit human approval'})
    return approval

def check_approval(plan,when):
    aid=plan.get('approval_id');
    if not aid: raise RuntimeError('Plan has no approval')
    approval=read(approval_path(aid),{})
    if approval.get('status')!='APPROVED' or approval.get('plan_id')!=plan['plan_id'] or approval.get('review_hash')!=plan['review_hash']: raise RuntimeError('Approval is invalid')
    if datetime.fromisoformat(approval['expires_utc'])<when: raise RuntimeError('Approval expired')
    return approval

def backup(paths,tid):
    root=BACKUP_DIR/('promotion_block7_'+tid); root.mkdir(parents=True,exist_ok=False); entries=[]
    for path in paths:
        e={'path':str(path),'existed':path.exists()}
        if path.exists():
            dst=root/'files'/str(path).lstrip('/'); dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(path,dst); e['backup_path']=str(dst)
        entries.append(e)
    atomic(root/'manifest.json',{'transaction_id':tid,'created_utc':iso(),'entries':entries}); return root

def restore(root):
    doc=read(root/'manifest.json',{'entries':[]})
    for e in doc['entries']:
        path=Path(e['path'])
        if e['existed']:
            path.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(e['backup_path'],path)
        elif path.exists(): path.unlink()

def update_runtime_registry(status,candidate_id):
    doc=read(CANDIDATE_REGISTRY_PATH,{'candidates':[]}); found=False
    for row in doc.get('candidates',[]):
        if row.get('strategy_id')==candidate_id:
            row['status']=status; row.setdefault('metadata',{})['role']=status+'_PAPER'; row['metadata']['enabled']=True; found=True
    if not found: raise RuntimeError('Candidate registry row missing')
    doc['block7_updated_utc']=iso(); doc['automatic_promotions']=0; atomic(CANDIDATE_REGISTRY_PATH,doc)

def execute(plan_id,confirmation,executed_by,when=None):
    current=when or now(); doc,plan=find_plan(plan_id); verify_fresh(plan)
    if plan.get('status')!='APPROVED': raise RuntimeError('Plan must be APPROVED')
    if confirmation!=plan.get('execute_confirmation'): raise RuntimeError('Exact execute confirmation does not match')
    approval=check_approval(plan,current)
    if config().get('require_flat_parent_and_candidate',True):
        if open_count(plan['candidate_portfolio']) or open_count(plan['parent_portfolio']): raise RuntimeError('Candidate and parent must have zero open positions')
    tid='TX-'+uuid.uuid4().hex[:20].upper(); paths=[PLANS_PATH,PROMOTION_STATE_PATH,CANDIDATE_STATE_PATH,CANDIDATE_REGISTRY_PATH,REGISTRY_PATH,HISTORY_PATH]
    root=backup(paths,tid)
    try:
        cdoc=read(CANDIDATE_STATE_PATH,{'candidates':{}}); cand=cdoc.get('candidates',{}).get(plan['candidate_id'])
        if not isinstance(cand,dict) or cand.get('status','CANDIDATE') not in {'CANDIDATE','SHADOW','EX_MASTER'}: raise RuntimeError('Candidate runtime state is not promotable')
        cand['status']='MASTER'; cand['active']=True; cand['portfolio_definition']['is_main']=True; cand['portfolio_definition']['compact_shadow']=False; cand['portfolio_definition']['evolution_status']='MASTER'; cand['promotion_transaction_id']=tid; atomic(CANDIDATE_STATE_PATH,cdoc)
        update_runtime_registry('MASTER',plan['candidate_id'])
        reg=registry(); life=StrategyLifecycleManager(reg); crecord=reg.get(plan['candidate_id']); parent=reg.get(plan['parent_id'])
        if crecord.family_id!=parent.family_id: raise RuntimeError('Candidate and parent family mismatch')
        if parent.status!=StrategyStatus.MASTER: raise RuntimeError(f'Parent is not MASTER: {parent.status.value}')
        if crecord.status==StrategyStatus.CANDIDATE: life.transition(crecord.strategy_id,StrategyStatus.SHADOW,'block7_pre_promotion',{'plan_id':plan_id,'transaction_id':tid})
        crecord=reg.get(crecord.strategy_id)
        if crecord.status in {StrategyStatus.SHADOW,StrategyStatus.EX_MASTER}: life.transition(crecord.strategy_id,StrategyStatus.MASTER,'block7_human_approved_promotion',{'plan_id':plan_id,'transaction_id':tid,'approved_by':approval['approved_by']})
        if reg.get(parent.strategy_id).status!=StrategyStatus.EX_MASTER or reg.get(crecord.strategy_id).status!=StrategyStatus.MASTER: raise RuntimeError('Evolution Core lifecycle transition incomplete')
        pstate=read(PROMOTION_STATE_PATH,{'schema_version':1,'active_by_family':{},'transactions':[]})
        tx={'transaction_id':tid,'plan_id':plan_id,'candidate_id':plan['candidate_id'],'candidate_portfolio':plan['candidate_portfolio'],'parent_id':plan['parent_id'],'parent_portfolio':plan['parent_portfolio'],'family_id':plan['family_id'],'status':'EXECUTED','executed_utc':iso(current),'executed_by':executed_by,'approved_by':approval['approved_by'],'review_hash':plan['review_hash'],'rollback_deadline_utc':iso(current+timedelta(days=int(config().get('rollback_window_days',30)))),'backup':str(root),'paper_only':True,'live_modified':False,'orders_sent':False}
        pstate.setdefault('active_by_family',{})[plan['family_id']]=tx; pstate.setdefault('transactions',[]).append(tx); pstate.update({'updated_utc':iso(current),'automatic_promotions':0,'automatic_rollbacks':0,'live_modified':False,'orders_sent':False}); atomic(PROMOTION_STATE_PATH,pstate)
        plan.update({'status':'EXECUTED','transaction_id':tid,'executed_utc':iso(current),'executed_by':executed_by,'updated_utc':iso(current)}); save_plans(doc); atomic(transaction_path(tid),tx)
        append_event({'generated_utc':iso(current),'event_type':'PROMOTION_EXECUTED','plan_id':plan_id,'candidate_id':plan['candidate_id'],'candidate_portfolio':plan['candidate_portfolio'],'parent_id':plan['parent_id'],'parent_portfolio':plan['parent_portfolio'],'family_id':plan['family_id'],'old_status':'APPROVED','new_status':'EXECUTED','review_hash':plan['review_hash'],'transaction_id':tid,'approved_by':approval['approved_by'],'reason':'Explicit human-approved Paper promotion'})
        return tx
    except Exception:
        restore(root); raise

def rollback(transaction_id,confirmation,rolled_back_by,reason,when=None):
    current=when or now(); tx=read(transaction_path(transaction_id),{})
    if tx.get('status')!='EXECUTED': raise RuntimeError('Transaction is not executable for rollback')
    if confirmation!=f'ROLLBACK {transaction_id}': raise RuntimeError('Exact rollback confirmation does not match')
    if datetime.fromisoformat(tx['rollback_deadline_utc'])<current: raise RuntimeError('Rollback window expired')
    if config().get('require_flat_parent_and_candidate',True):
        if open_count(tx['candidate_portfolio']) or open_count(tx['parent_portfolio']): raise RuntimeError('Candidate and parent must have zero open positions')
    rid='RB-'+uuid.uuid4().hex[:20].upper(); paths=[PLANS_PATH,PROMOTION_STATE_PATH,CANDIDATE_STATE_PATH,CANDIDATE_REGISTRY_PATH,REGISTRY_PATH,HISTORY_PATH,transaction_path(transaction_id)]
    root=backup(paths,rid)
    try:
        cdoc=read(CANDIDATE_STATE_PATH,{'candidates':{}}); cand=cdoc.get('candidates',{}).get(tx['candidate_id'])
        if not isinstance(cand,dict): raise RuntimeError('Candidate runtime state missing')
        cand['status']='EX_MASTER'; cand['active']=True; cand['portfolio_definition']['is_main']=False; cand['portfolio_definition']['compact_shadow']=True; cand['portfolio_definition']['evolution_status']='EX_MASTER'; cand['rollback_transaction_id']=rid; atomic(CANDIDATE_STATE_PATH,cdoc); update_runtime_registry('EX_MASTER',tx['candidate_id'])
        reg=registry(); life=StrategyLifecycleManager(reg); parent=reg.get(tx['parent_id']); candidate_record=reg.get(tx['candidate_id'])
        if parent.status!=StrategyStatus.EX_MASTER or candidate_record.status!=StrategyStatus.MASTER: raise RuntimeError('Evolution Core roles are not rollback-ready')
        life.transition(parent.strategy_id,StrategyStatus.MASTER,'block7_explicit_rollback',{'transaction_id':transaction_id,'rollback_id':rid,'rolled_back_by':rolled_back_by,'reason':reason})
        if reg.get(parent.strategy_id).status!=StrategyStatus.MASTER or reg.get(candidate_record.strategy_id).status!=StrategyStatus.EX_MASTER: raise RuntimeError('Rollback lifecycle transition incomplete')
        pstate=read(PROMOTION_STATE_PATH,{'active_by_family':{},'transactions':[]}); pstate.get('active_by_family',{}).pop(tx['family_id'],None)
        for row in pstate.get('transactions',[]):
            if row.get('transaction_id')==transaction_id: row.update({'status':'ROLLED_BACK','rolled_back_utc':iso(current),'rollback_id':rid,'rolled_back_by':rolled_back_by,'rollback_reason':reason})
        pstate['updated_utc']=iso(current); atomic(PROMOTION_STATE_PATH,pstate)
        doc,plan=find_plan(tx['plan_id']); plan.update({'status':'ROLLED_BACK','rollback_id':rid,'rolled_back_utc':iso(current),'rolled_back_by':rolled_back_by,'updated_utc':iso(current)}); save_plans(doc)
        tx.update({'status':'ROLLED_BACK','rolled_back_utc':iso(current),'rollback_id':rid,'rolled_back_by':rolled_back_by,'rollback_reason':reason}); atomic(transaction_path(transaction_id),tx)
        append_event({'generated_utc':iso(current),'event_type':'PROMOTION_ROLLED_BACK','plan_id':tx['plan_id'],'candidate_id':tx['candidate_id'],'candidate_portfolio':tx['candidate_portfolio'],'parent_id':tx['parent_id'],'parent_portfolio':tx['parent_portfolio'],'family_id':tx['family_id'],'old_status':'EXECUTED','new_status':'ROLLED_BACK','review_hash':tx['review_hash'],'transaction_id':transaction_id,'approved_by':rolled_back_by,'reason':reason})
        return tx
    except Exception:
        restore(root); raise

def locked():
    LOCK_PATH.parent.mkdir(parents=True,exist_ok=True); handle=LOCK_PATH.open('a+'); fcntl.flock(handle.fileno(),fcntl.LOCK_EX); return handle

def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('list')
    a=sub.add_parser('approve'); a.add_argument('--plan-id',required=True); a.add_argument('--approved-by',required=True); a.add_argument('--confirmation',required=True)
    e=sub.add_parser('execute'); e.add_argument('--plan-id',required=True); e.add_argument('--executed-by',required=True); e.add_argument('--confirmation',required=True)
    r=sub.add_parser('rollback'); r.add_argument('--transaction-id',required=True); r.add_argument('--rolled-back-by',required=True); r.add_argument('--reason',required=True); r.add_argument('--confirmation',required=True)
    args=p.parse_args(); h=locked()
    try:
        if args.cmd=='list': result=list_plans()
        elif args.cmd=='approve': result=approve(args.plan_id,args.approved_by,args.confirmation)
        elif args.cmd=='execute': result=execute(args.plan_id,args.confirmation,args.executed_by)
        else: result=rollback(args.transaction_id,args.confirmation,args.rolled_back_by,args.reason)
        print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)); return 0
    except Exception as exc:
        print(f'Block 7 administration failed: {exc}'); return 2
    finally:
        h.close()
if __name__=='__main__': raise SystemExit(main())
