# main.py

from src.client import fetch_emails

def main():
    emails = fetch_emails()
    
    for email in emails:
        print(email["subject"])

if __name__ == "__main__":
    main()