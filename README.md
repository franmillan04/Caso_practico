# Email Prioritization Pipeline

Este proyecto implementa un sistema completo de procesamiento y priorización de emails utilizando FastAPI, limpieza de texto con expresiones regulares, análisis con LLM local (Ollama) y visualización en Streamlit.

---

# Objetivo del proyecto

La empresa recibe emails sin ningún tipo de priorización. Este sistema:

1. Expone emails mediante una API local
2. Limpia el contenido de los emails
3. Analiza los emails con un modelo LLM local
4. Calcula una puntuación de urgencia
5. Muestra una cola de prioridad en una interfaz web

---

# Arquitectura del proyecto (Por el momento)
Email Prioritization Pipeline

src/
- api.py        → FastAPI API que expone emails
- client.py     → Cliente para consumir API

data/
- emails.py     → MOCK_EMAILS

main.py         → Ejecuta el pipeline completo

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
pip install fastapi uvicorn requests ollama streamlit
```

# Ejecución del proyecto
## 1. Levantar API
```bash
uvicorn src.api:app --reload
```
API disponible en:

- http://127.0.0.1:8000/emails
- http://127.0.0.1:8000/docs

## 2. Configuración de Ollama
1. Descargar **Ollama** desde su página oficial: https://ollama.com/download
2. Instalar el modelo *gemma3:1b* a través del siguiente comando:
    ```bash
    ollama pull gemma3:1b
    ```

## 3. Ejecutar pipeline (opcional para comprobar que funciona)
```bash
python main.py
```
Esto ejecuta el consumo de API, con:
    Limpia emails

    Llama al LLM

    Calcula score

    Muestra ranking por prioridad

## 4. Ejecutar dashboard (Streamlit)
```bash
streamlit run app.py
```
Esto levanta una aplicación web local donde se muestra la cola de prioridad de emails y permite ajustar los pesos del scoring en tiempo real.


