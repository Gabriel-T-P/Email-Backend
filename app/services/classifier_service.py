def classify_email(text: str) -> dict:
    """
    Mock de classificação.
    Futuramente, vai usar um modelo ML.
    """

    # Regra simples só para exemplo
    if "feliz" in text.lower() or "obrigado" in text.lower():
        category = "Improdutivo"
        response = "Obrigado pela sua mensagem!"
    else:
        category = "Produtivo"
        response = "Recebemos sua solicitação e em breve retornaremos."

    return {
        "category": category,
        "response": response
    }
