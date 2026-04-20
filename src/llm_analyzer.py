# src/llm_analyzer.py
import json
import re
import ollama

MODEL_NAME = "gemma3:1b"

SYSTEM_PROMPT = """
Eres un analizador de emails. Devuelve SOLO JSON válido con esta estructura:
{
  "sentiment": "positive|neutral|negative",
  "topic": "texto corto",
  "summary": "resumen breve en español",
  "confidence": 0.0
}
No añadas texto extra, markdown ni explicaciones.
"""

def _extract_json(text: str):
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not match:
        raise ValueError("No se encontró JSON en la respuesta del modelo")
    return json.loads(match.group(0))

def analyze_email(subject: str, body: str):
    prompt = f"""
Asunto: {subject}
Cuerpo: {body}
"""
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    content = response["message"]["content"] if isinstance(response, dict) else response.message.content
    data = _extract_json(content)

    return {
        "sentiment": data.get("sentiment", "neutral"),
        "topic": data.get("topic", ""),
        "summary": data.get("summary", ""),
        "confidence": float(data.get("confidence", 0.0)),
    }

def analyze_emails(processed_emails):
    results = []
    for email in processed_emails:
        analysis = analyze_email(email["subject"], email["body"])
        results.append({
            **email,
            **analysis
        })
    return results