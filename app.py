import streamlit as st
import pandas as pd
from main import main
from src.scoring import compute_score

st.title("📧 Email Prioritization System")

# ejecutar pipeline
_, emails = main()

st.sidebar.header("⚙️ Ajuste de pesos")

w_sent = st.sidebar.slider("Sentimiento", 0.0, 1.0, 0.4)
w_topic = st.sidebar.slider("Tema", 0.0, 1.0, 0.4)
w_conf = st.sidebar.slider("Confianza", 0.0, 1.0, 0.2)

# normalizar
total = w_sent + w_topic + w_conf
w_sent /= total
w_topic /= total
w_conf /= total

# recalcular scores dinámicamente
for email in emails:
    email["score"] = compute_score(email, w_sent, w_topic, w_conf)

emails_sorted = sorted(emails, key=lambda x: x["score"], reverse=True)

df = pd.DataFrame(emails_sorted)

st.subheader("📊 Cola de prioridad")
st.dataframe(df[[
    "subject",
    "sentiment",
    "topic",
    "confidence",
    "score"
]])

st.subheader("🚨 Top 3 más urgentes")

for email in emails_sorted[:3]:
    st.markdown(f"### {email['subject']}")
    st.write(f"Score: {email['score']}")
    st.write(email["summary"])