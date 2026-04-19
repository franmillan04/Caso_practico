# main.py

from src.client import fetch_emails

def get_subject(email):
    headers = email.get("payload", {}).get("headers", [])
    
    for h in headers:
        if h["name"].lower() == "subject":
            return h["value"]
    
    return "Sin asunto"

def main():
    emails = fetch_emails()
    
    for email in emails:
        print(get_subject(email))

if __name__ == "__main__":
    main()