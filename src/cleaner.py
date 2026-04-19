import re

def clean_html(text: str) -> str:
    # Quitar HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    
    # Quitar entidades HTML (&nbsp;, etc.)
    text = re.sub(r"&\w+;", " ", text)
    
    return text


def remove_urls(text: str) -> str:
    # quitar URLs
    text = re.sub(r"http\S+|www\.\S+", "", text)

    # dividir en líneas y limpiar basura colgada
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        line_clean = re.sub(
            r"\b(register here|click here|more info|link here)\b[:\-]?\s*",
            "",
            line,
            flags=re.IGNORECASE
        ).strip()

        if len(line_clean) > 0:
            cleaned_lines.append(line_clean)

    return " ".join(cleaned_lines)


def remove_emails(text: str) -> str:
    return re.sub(r"\S+@\S+", " ", text)


def remove_phone_numbers(text: str) -> str:
    return re.sub(r"\+?\d[\d\s\-\(\)]{7,}\d", " ", text)


def remove_quotes(text: str) -> str:
    # elimina líneas tipo "> On Mon..."
    return re.sub(r"^>.*$", " ", text, flags=re.MULTILINE)


def remove_signatures(text: str) -> str:
    patterns = [
        r"Sent from my iPhone",
        r"--\s*",
        r"---------- Forwarded message ---------",
        r"This email and any attachments are confidential.*",
        r"\[.*?REDACTED.*?\]"
    ]

    for p in patterns:
        text = re.sub(p, " ", text, flags=re.IGNORECASE)

    return text


def normalize_whitespace(text: str) -> str:
    # limpiar espacios extra
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_email(text: str) -> str:
    """
    Pipeline completo de limpieza
    """
    text = clean_html(text)
    text = remove_urls(text)
    text = remove_emails(text)
    text = remove_phone_numbers(text)
    text = remove_quotes(text)
    text = remove_signatures(text)
    text = normalize_whitespace(text)
    
    return text