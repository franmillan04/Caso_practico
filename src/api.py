# src/api.py

from fastapi import FastAPI
from data.emails import MOCK_EMAILS

app = FastAPI()

@app.get("/emails")
def get_emails():
    return MOCK_EMAILS