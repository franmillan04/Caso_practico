from src.client import fetch_emails
from src.cleaner import clean_email


def get_subject(email):
    headers = email.get("payload", {}).get("headers", [])

    for h in headers:
        if h["name"].lower() == "subject":
            return h["value"]

    return "Sin asunto"


def main():
    emails = fetch_emails()

    processed_emails = []

    for email in emails:
        subject = get_subject(email)
        raw_body = email.get("body_text_content", "")
        clean_body = clean_email(raw_body)

        processed_email = {
            "id": email.get("id"),
            "subject": subject,
            "body": clean_body
        }

        processed_emails.append(processed_email)

        print("\n--- EMAIL PROCESADO ---")
        print("Subject:", subject)
        print("Body:", clean_body)

    return processed_emails

if __name__ == "__main__":
    main()