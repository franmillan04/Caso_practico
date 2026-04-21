from src.client import fetch_emails
from src.cleaner import clean_email
from src.llm_analyzer import analyze_emails
from src.scoring import compute_score


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
    
    print("\nANALIZANDO CON LLM...")
    final_emails = analyze_emails(processed_emails)

    print("\nCALCULANDO SCORES...")

    for email in final_emails:
        email["score"] = compute_score(email)
    
    # ordenar por prioridad
    final_emails = sorted(final_emails, key=lambda x: x["score"], reverse=True)

    print("\nRESULTADOS CON PRIORIDAD:")
    for email in final_emails:
        print(f"\nID: {email['id']}")
        print(f"Score: {email['score']}")
        print(f"Sentimiento: {email.get('sentiment')}")
        print(f"Tema: {email.get('topic')}")
        print(f"Resumen: {email.get('summary')}")

if __name__ == "__main__":
    main()