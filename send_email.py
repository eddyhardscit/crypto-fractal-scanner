import os
import smtplib
from datetime import datetime, timezone
from email.message import EmailMessage


REPORT_PATH = "reports/latest_report.md"

DEFAULT_REPORT_URL = (
    "https://github.com/eddyhardscit/crypto-fractal-scanner/"
    "blob/main/reports/latest_report.md"
)


def extract_fast_reading(report_text):
    """
    Prende dal report solo la parte 'Lettura velocissima',
    così l'email non diventa lunghissima.
    """
    possible_titles = [
        "# Lettura velocissima",
        "## Lettura velocissima",
    ]

    start = -1

    for title in possible_titles:
        start = report_text.find(title)
        if start != -1:
            break

    if start == -1:
        return report_text[:3000]

    end = report_text.find("\n---", start)

    if end == -1:
        end = start + 4000

    summary = report_text[start:end].strip()

    if len(summary) > 4000:
        summary = summary[:4000] + "\n\n[Riassunto tagliato: apri il report completo.]"

    return summary


def main():
    email_user = os.environ.get("EMAIL_USER")
    email_password = os.environ.get("EMAIL_PASSWORD")
    email_to = os.environ.get("EMAIL_TO")
    report_url = os.environ.get("REPORT_URL", DEFAULT_REPORT_URL)

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

    fast_reading = extract_fast_reading(report_text)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    subject = f"Crypto Scanner — Report giornaliero {today}"

    body = f"""Report crypto aggiornato.

Link al report completo:
{report_url}

In allegato trovi anche il file latest_report.md.

------------------------------

{fast_reading}

------------------------------

Nota:
Il report è statistico, non è una previsione certa.
Guarda soprattutto:
- direzione più probabile;
- casi positivi / negativi;
- return 30d;
- drawdown 30d;
- max gain 30d.
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

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(email_user, email_password)
        smtp.send_message(msg)

    print("Email sent successfully.")


if __name__ == "__main__":
    main()
