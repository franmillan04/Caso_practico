from src.client import fetch_emails
from src.cleaner import clean_email
from src.llm_analyzer import analyze_emails


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
    
    # MOSTRAR RESULTADOS FINALES
    print("\nRESULTADOS COMPLETOS:")
    for email in final_emails[:3]:  # Solo primeros 3 para no saturar
        print(f"\nID: {email['id']}")
        print(f"Sentimiento: {email.get('sentiment', 'N/A')}")
        print(f"Tema: {email.get('topic', 'N/A')}")
        print(f"Resumen: {email.get('summary', 'N/A')}")
        print(f"Confianza: {email.get('confidence', 0):.2f}")

    return processed_emails, final_emails

if __name__ == "__main__":
    main()