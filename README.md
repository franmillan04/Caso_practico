# Email Prioritization Pipeline

Este proyecto implementa un sistema completo de procesamiento y priorización de emails utilizando FastAPI, limpieza de texto con expresiones regulares, análisis con LLM local (Ollama) y visualización en Streamlit.

---

# 🎯 Objetivo del proyecto

La empresa recibe emails sin ningún tipo de priorización. Este sistema:

1. Expone emails mediante una API local
2. Limpia el contenido de los emails
3. Analiza los emails con un modelo LLM local
4. Calcula una puntuación de urgencia
5. Muestra una cola de prioridad en una interfaz web

---

# 🧱 Arquitectura del proyecto (Por el momento)
├── src/
│   ├── api.py        # FastAPI API que expone los emails
│   ├── client.py     # Cliente para consumir la API
│
├── data/
│   ├── emails.py     # Datos MOCK_EMAILS
│
├── main.py        # Orquestador del pipeline completo

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/franmillan04/Caso_practico.git
cd Caso_practico
```

## 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

## 3. Instalar dependencias (Por el momento)
```bash
pip install fastapi uvicorn requests
```

# Ejecución del proyecto
## 1. Levantar API
```bash
uvicorn src.api:app --reload
```
API disponible en:

- http://127.0.0.1:8000/emails
- http://127.0.0.1:8000/docs

## 2. Ejecutar pipeline completo
```bash
python main.py
```
Esto ejecuta el consumo de API


