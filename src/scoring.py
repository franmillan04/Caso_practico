# src/scoring.py

def map_sentiment(sentiment: str) -> float:
    return {
        "positive": 0.2,
        "neutral": 0.5,
        "negative": 1.0
    }.get(sentiment, 0.5)


def map_topic(topic: str) -> float:
    topic = topic.lower()

    if "factur" in topic:
        return 1.0
    elif "soporte" in topic or "bug" in topic or "error" in topic:
        return 0.9
    elif "venta" in topic or "pricing" in topic:
        return 0.6
    elif "feedback" in topic or "idea" in topic:
        return 0.4
    else:
        return 0.5


def compute_score(email, w_sent=0.4, w_topic=0.4, w_conf=0.2):
    sentiment_score = map_sentiment(email.get("sentiment", "neutral"))
    topic_score = map_topic(email.get("topic", ""))
    confidence = email.get("confidence", 0.0)

    score = (
        w_sent * sentiment_score +
        w_topic * topic_score +
        w_conf * confidence
    )

    return round(score, 3)