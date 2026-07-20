#!/usr/bin/env python3
"""Inventario read-only dell'ecosistema crypto scanner.

Scopre:
- portafogli paper e ruoli (MAIN/PAPER/SHADOW/TEST)
- strategie referenziate
- Research Signal
- SOL Spot Adaptive e altri bot/runner separati
- servizi systemd collegati al repository
- workflow GitHub Actions
- possibili entry point Python

Scrive soltanto:
- reports/evolution_inventory.json
- reports/evolution_inventory.md

Non importa moduli del progetto, non modifica configurazioni, non riavvia servizi
ed esegue zero ordini.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

EXCLUDED_DIRS = {
    ".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
    "scanner_backups", "evolution_install", ".venv", "venv", "node_modules",
}
SOURCE_SUFFIXES = {".py", ".yml", ".yaml", ".json", ".md", ".service", ".sh"}
PATTERNS = {
    "paper": re.compile(r"paper[_ -]?(?:trading|signal)", re.I),
    "shadow": re.compile(r"\bshadow\b|compact_shadow", re.I),
    "research": re.compile(
        r"research[_ -]?signal|research_signals|run_research_cycle|research_sample",
        re.I,
    ),
    "sol_spot_adaptive": re.compile(r"sol[_ -]?spot[_ -]?adaptive", re.I),
    "live": re.compile(r"real_orders_enabled|live[_ -]?trading|kucoin.*order", re.I),
    "telegram": re.compile(r"telegram|send_text|chat_id", re.I),
}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_read(path: Path, max_bytes: int = 2_000_000) -> str:
    try:
        if path.stat().st_size > max_bytes:
            return ""
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def iter_files(root: Path) -> Iterable[Path]:
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        base = Path(current_root)
        for filename in files:
            path = base / filename
            if path.suffix.lower() in SOURCE_SUFFIXES:
                yield path


def role_for(portfolio: dict[str, Any]) -> str:
    name = str(portfolio.get("name", "")).upper()
    if bool(portfolio.get("paper_only_high_leverage_test")):
        return "TEST"
    if bool(portfolio.get("compact_shadow")) or name.startswith("SHADOW_"):
        return "SHADOW"
    if portfolio.get("is_main") is True:
        return "MAIN"
    return "PAPER"


def load_portfolios(repo: Path) -> tuple[list[dict[str, Any]], list[str]]:
    path = repo / "paper_trading_config.json"
    if not path.exists():
        return [], ["paper_trading_config.json non trovato"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [], [f"paper_trading_config.json non leggibile: {exc}"]

    raw = data.get("portfolios", [])
    if not isinstance(raw, list):
        return [], ["La chiave portfolios non contiene una lista"]

    result: list[dict[str, Any]] = []
    warnings: list[str] = []
    for index, item in enumerate(raw):
        if not isinstance(item, dict):
            warnings.append(f"Portfolio {index}: valore non valido")
            continue
        result.append({
            "index": index,
            "name": str(item.get("name", "")).strip(),
            "strategy": str(item.get("strategy", "")).strip(),
            "enabled": bool(item.get("enabled", False)),
            "role": role_for(item),
            "is_main": item.get("is_main"),
            "compact_shadow": item.get("compact_shadow"),
            "timeframe_minutes": item.get("timeframe_minutes"),
            "leverage": item.get("leverage"),
            "max_leverage": item.get("max_leverage"),
            "fixed_margin_eur": item.get("fixed_margin_eur"),
        })
    return result, warnings


def scan_sources(repo: Path) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    for path in iter_files(repo):
        text = safe_read(path)
        if not text:
            continue
        categories = sorted(k for k, pattern in PATTERNS.items() if pattern.search(text))
        if not categories:
            continue
        entrypoint = bool(
            path.suffix == ".py"
            and ("if __name__" in text or re.search(r"^\s*def\s+main\s*\(", text, re.M))
        )
        found.append({
            "path": str(path.relative_to(repo)),
            "categories": categories,
            "likely_entrypoint": entrypoint,
            "size_bytes": path.stat().st_size,
        })
    return sorted(found, key=lambda x: x["path"])


def systemd_services(repo: Path) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    seen: set[str] = set()
    for base in (Path("/etc/systemd/system"), Path("/lib/systemd/system"), Path("/usr/lib/systemd/system")):
        if not base.exists():
            continue
        for path in base.rglob("*.service"):
            key = str(path)
            if key in seen:
                continue
            seen.add(key)
            text = safe_read(path, 500_000)
            if not text:
                continue
            exec_start = [
                line.strip().split("=", 1)[1]
                for line in text.splitlines()
                if line.strip().startswith("ExecStart=")
            ]
            working = next((
                line.strip().split("=", 1)[1]
                for line in text.splitlines()
                if line.strip().startswith("WorkingDirectory=")
            ), None)
            haystack = "\n".join(exec_start + [working or ""]).lower()
            if not (
                str(repo).lower() in haystack
                or "crypto-fractal-scanner" in haystack
                or "paper_trading" in haystack
                or "sol_spot_adaptive" in haystack
            ):
                continue
            results.append({
                "unit": path.name,
                "path": str(path),
                "working_directory": working,
                "exec_start": exec_start,
            })
    return sorted(results, key=lambda x: x["unit"])


def cron_entries(repo: Path) -> list[dict[str, str]]:
    sources: list[tuple[str, str]] = []
    try:
        proc = subprocess.run(
            ["crontab", "-l"], capture_output=True, text=True, timeout=10, check=False
        )
        if proc.returncode == 0:
            sources.append(("root_crontab", proc.stdout))
    except Exception:
        pass

    for path in [Path("/etc/crontab")]:
        if path.exists():
            sources.append((str(path), safe_read(path, 500_000)))
    if Path("/etc/cron.d").exists():
        for path in Path("/etc/cron.d").iterdir():
            if path.is_file():
                sources.append((str(path), safe_read(path, 500_000)))

    results: list[dict[str, str]] = []
    for source, text in sources:
        for raw in text.splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            lower = line.lower()
            if (
                str(repo).lower() in lower
                or "crypto-fractal-scanner" in lower
                or "paper_trading" in lower
                or "sol_spot_adaptive" in lower
            ):
                results.append({"source": source, "entry": line})
    return results


def workflows(repo: Path) -> list[dict[str, Any]]:
    base = repo / ".github" / "workflows"
    if not base.exists():
        return []
    results = []
    for path in sorted(base.glob("*.y*ml")):
        text = safe_read(path)
        categories = sorted(k for k, p in PATTERNS.items() if p.search(text))
        results.append({"path": str(path.relative_to(repo)), "categories": categories})
    return results


def build_report(repo: Path) -> dict[str, Any]:
    portfolios, warnings = load_portfolios(repo)
    sources = scan_sources(repo)
    services = systemd_services(repo)
    cron = cron_entries(repo)
    flows = workflows(repo)

    role_counts = Counter(p["role"] for p in portfolios)
    strategy_counts = Counter(p["strategy"] for p in portfolios if p["strategy"])
    names = [p["name"] for p in portfolios if p["name"]]
    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)

    research = [x for x in sources if "research" in x["categories"]]
    shadow = [x for x in sources if "shadow" in x["categories"]]
    adaptive = [x for x in sources if "sol_spot_adaptive" in x["categories"]]
    live = [x for x in sources if "live" in x["categories"]]
    entrypoints = [x for x in sources if x["likely_entrypoint"]]

    return {
        "schema_version": 1,
        "generated_at": utc_now_iso(),
        "repository": str(repo),
        "safety": {
            "read_only": True,
            "project_modules_imported": False,
            "services_restarted": False,
            "trading_configuration_changed": False,
        },
        "summary": {
            "portfolio_count": len(portfolios),
            "role_counts": dict(sorted(role_counts.items())),
            "enabled_count": sum(1 for p in portfolios if p["enabled"]),
            "disabled_count": sum(1 for p in portfolios if not p["enabled"]),
            "unique_strategy_count": len(strategy_counts),
            "research_related_files": len(research),
            "shadow_related_files": len(shadow),
            "sol_spot_adaptive_files": len(adaptive),
            "live_related_candidates": len(live),
            "systemd_service_count": len(services),
            "cron_entry_count": len(cron),
            "workflow_count": len(flows),
            "likely_entrypoint_count": len(entrypoints),
        },
        "validation": {
            "warnings": warnings,
            "duplicate_portfolio_names": duplicates,
            "missing_name_indexes": [p["index"] for p in portfolios if not p["name"]],
            "missing_strategy_indexes": [p["index"] for p in portfolios if not p["strategy"]],
        },
        "portfolios": portfolios,
        "strategy_variant_counts": dict(sorted(strategy_counts.items())),
        "research_signal": {
            "detected": bool(research),
            "files": research,
            "integration_rule": (
                "Collegare Research Signal alle strategie/segnali originali; non creare doppioni "
                "se è uno strato di ricerca e selezione."
            ),
        },
        "shadow": {"portfolio_count": role_counts.get("SHADOW", 0), "files": shadow},
        "sol_spot_adaptive": {"detected": bool(adaptive), "files": adaptive},
        "live_candidates": {
            "files": live,
            "rule": "Esclusi da mutazioni e promozioni automatiche finché non validati nel paper.",
        },
        "systemd_services": services,
        "cron_entries": cron,
        "workflows": flows,
        "likely_entrypoints": entrypoints,
    }


def md(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(report: dict[str, Any]) -> str:
    s = report["summary"]
    lines = [
        "# Evolution Ecosystem Inventory",
        "",
        f"Generato: `{report['generated_at']}`",
        f"Repository: `{report['repository']}`",
        "",
        "> Inventario in sola lettura: nessun servizio riavviato e nessuna configurazione di trading modificata.",
        "",
        "## Riepilogo",
        "",
        f"- Portafogli: **{s['portfolio_count']}**",
        f"- Ruoli: `{json.dumps(s['role_counts'], ensure_ascii=False, sort_keys=True)}`",
        f"- Strategie uniche: **{s['unique_strategy_count']}**",
        f"- File Research: **{s['research_related_files']}**",
        f"- File Shadow: **{s['shadow_related_files']}**",
        f"- File SOL Spot Adaptive: **{s['sol_spot_adaptive_files']}**",
        f"- Servizi systemd collegati: **{s['systemd_service_count']}**",
        f"- Cron collegati: **{s['cron_entry_count']}**",
        f"- Entry point probabili: **{s['likely_entrypoint_count']}**",
        "",
        "## Portafogli",
        "",
        "| # | Nome | Strategia | Ruolo | Attivo | TF | Leva |",
        "|---:|---|---|---|:---:|---:|---:|",
    ]
    for p in report["portfolios"]:
        lines.append(
            f"| {p['index']} | {md(p['name'])} | {md(p['strategy'])} | {p['role']} | "
            f"{'sì' if p['enabled'] else 'no'} | {md(p['timeframe_minutes'])} | {md(p['leverage'])} |"
        )

    lines += ["", "## Strategie e varianti", "", "| Strategia | Varianti |", "|---|---:|"]
    for strategy, count in report["strategy_variant_counts"].items():
        lines.append(f"| {md(strategy)} | {count} |")

    lines += ["", "## Research Signal", "", report["research_signal"]["integration_rule"], ""]
    for item in report["research_signal"]["files"]:
        lines.append(f"- `{item['path']}`")

    lines += ["", "## SOL Spot Adaptive", ""]
    for item in report["sol_spot_adaptive"]["files"]:
        lines.append(f"- `{item['path']}`")

    lines += ["", "## Servizi systemd", ""]
    if report["systemd_services"]:
        for item in report["systemd_services"]:
            lines.append(f"- `{item['unit']}` — directory: `{item.get('working_directory')}`")
            for cmd in item.get("exec_start", []):
                lines.append(f"  - `{md(cmd)}`")
    else:
        lines.append("- Nessun servizio collegato rilevato.")

    lines += ["", "## Entry point probabili", ""]
    for item in report["likely_entrypoints"]:
        lines.append(f"- `{item['path']}` — {', '.join(item['categories'])}")

    lines += [
        "", "## Validazione", "",
        f"- Nomi duplicati: `{report['validation']['duplicate_portfolio_names']}`",
        f"- Indici senza nome: `{report['validation']['missing_name_indexes']}`",
        f"- Indici senza strategia: `{report['validation']['missing_strategy_indexes']}`",
        "",
        "## Regola di integrazione",
        "",
        "Paper, Shadow, Research e bot separati devono essere tutti censiti. Research Signal viene collegato alle identità originali quando riusa gli stessi segnali, evitando doppioni. Il live resta escluso dall'evoluzione automatica.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=".")
    parser.add_argument("--json-output", default="reports/evolution_inventory.json")
    parser.add_argument("--markdown-output", default="reports/evolution_inventory.md")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        raise SystemExit(f"Repository non trovato: {repo}")

    json_path = repo / args.json_output
    md_path = repo / args.markdown_output
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    report = build_report(repo)
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(report) + "\n", encoding="utf-8")

    s = report["summary"]
    print("=== EVOLUTION ECOSYSTEM INVENTORY ===")
    print(f"Repository: {repo}")
    print(f"Portafogli: {s['portfolio_count']}")
    print(f"Ruoli: {s['role_counts']}")
    print(f"Strategie uniche: {s['unique_strategy_count']}")
    print(f"File Research: {s['research_related_files']}")
    print(f"File Shadow: {s['shadow_related_files']}")
    print(f"File SOL Spot Adaptive: {s['sol_spot_adaptive_files']}")
    print(f"Servizi systemd: {s['systemd_service_count']}")
    print(f"Cron: {s['cron_entry_count']}")
    print(f"Entry point probabili: {s['likely_entrypoint_count']}")
    print(f"JSON: {json_path}")
    print(f"Markdown: {md_path}")
    print("Nessun servizio o parametro di trading è stato modificato.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
