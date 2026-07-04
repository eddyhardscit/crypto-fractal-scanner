import os
import smtplib
from datetime import datetime, timezone
from email.message import EmailMessage


REPORT_PATH = "reports/latest_report.md"
LIQ_REPORT_PATH = "reports/liquidation_report.md"

DEFAULT_REPORT_URL = (
    "https://github.com/eddyhardscit/crypto-fractal-scanner/"
    "blob/main/reports/latest_report.md"
)

DEFAULT_LIQ_REPORT_URL = (
    "https://github.com/eddyhardscit/crypto-fractal-scanner/"
    "blob/main/reports/liquidation_report.md"
)


def extract_section(report_text, titles, max_chars=4000):
    start = -1

    for title in titles:
        start = report_text.find(title)
        if start != -1:
            break

    if start == -1:
        return report_text[:max_chars]

    end_candidates = []

    next_hr = report_text.find("\n---", start + 1)
    if next_hr != -1:
        end_candidates.append(next_hr)

    next_h1 = report_text.find("\n# ", start + 1)
    if next_h1 != -1:
        end_candidates.append(next_h1)

    if end_candidates:
        end = min(end_candidates)
    else:
        end = start + max_chars

    section = report_text[start:end].strip()

    if len(section) > max_chars:
        section = section[:max_chars] + "\n\n[Sezione tagliata: apri il report completo.]"

    return section


def main():
    email_user = os.environ.get("EMAIL_USER")
    email_password = os.environ.get("EMAIL_PASSWORD")
    email_to = os.environ.get("EMAIL_TO")
    report_url = os.environ.get("REPORT_URL", DEFAULT_REPORT_URL)
    liq_report_url = os.environ.get("LIQ_REPORT_URL", DEFAULT_LIQ_REPORT_URL)

    if not email_user:
        raise RuntimeError("EMAIL_USER non trovato nei GitHub Secrets.")

    if not email_password:
        raise RuntimeError("EMAIL_PASSWORD non trovato nei GitHub Secrets.")

    if not email_to:
        raise RuntimeError("EMAIL_TO non trovato nei GitHub Secrets.")

    if not os.path.exists(REPORT_PATH):
        raise RuntimeError(f"Report non trovato: {REPORT_PATH}")

    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        report_text = f.read()

    fast_reading = extract_section(
        report_text,
        [
            "# Lettura velocissima",
            "## Lettura velocissima",
        ],
        max_chars=3500,
    )

    futures_summary = ""

    if "Sintesi futures / liquidazioni" in report_text:
        futures_summary = extract_section(
            report_text,
            [
                "# Sintesi futures / liquidazioni",
                "## Sintesi futures / liquidazioni",
            ],
            max_chars=2500,
        )

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    subject = f"Crypto Scanner — Report giornaliero {today}"

    body = f"""Report crypto aggiornato.

Link report frattale completo:
{report_url}

Link report liquidazioni/futures:
{liq_report_url}

In allegato trovi:
- latest_report.md
- liquidation_report.md, se generato correttamente

------------------------------
LETTURA VELOCE
------------------------------

{fast_reading}
"""

    if futures_summary:
        body += f"""

------------------------------
SINTESI FUTURES / LIQUIDAZIONI
------------------------------

{futures_summary}
"""

    body += """

------------------------------

Nota:
Il report è statistico, non è una previsione certa.
Per la leva guarda soprattutto:
- direzione frattale;
- drawdown 30d;
- funding;
- open interest;
- rischio flush sotto / short squeeze sopra.
"""

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_user
    msg["To"] = email_to
    msg.set_content(body)

    with open(REPORT_PATH, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="markdown",
            filename="latest_report.md",
        )

    if os.path.exists(LIQ_REPORT_PATH):
        with open(LIQ_REPORT_PATH, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="markdown",
                filename="liquidation_report.md",
            )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(email_user, email_password)
        smtp.send_message(msg)

    print("Email sent successfully.")


if __name__ == "__main__":
    main()
