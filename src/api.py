# src/api.py

from fastapi import FastAPI
from data.emails import MOCK_EMAILS

app = FastAPI()

@app.get("/emails")
def get_emails():
    return MOCK_EMAILS

@app.get("/emails/{email_id}")
def get_email(email_id: str):# si se pone como int devuelve none
    return next((e for e in MOCK_EMAILS if e["id"] == email_id), None)