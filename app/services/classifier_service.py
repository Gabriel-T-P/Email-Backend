import time

def classify_email(text: str) -> dict:
    start_time = time.time()
    word_count = len(text.split())

    # Mock: só para exemplo
    if "feliz" in text or "obrig" in text:
        category = "improdutivo"
        response = "Obrigado pela sua mensagem!"
        confidence = 0.9
    else:
        category = "produtivo"
        response = "Recebemos sua solicitação e em breve retornaremos."
        confidence = 0.85

    processing_time = (time.time() - start_time) * 1000  # ms

    return {
        "success": True,
        "data": {
            "classification": {
                "category": category,
                "confidence": confidence
            },
            "analysis": {
                "processingTime": round(processing_time, 2),
                "wordCount": word_count
            },
            "response": response
        },
        "error": None
    }
