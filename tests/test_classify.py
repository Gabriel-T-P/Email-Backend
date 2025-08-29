import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.parametrize(
    "text,expected_category",
    [
        ("Preciso de atualização do meu pedido", "Produtivo"),
        ("Feliz Natal a todos!", "Improdutivo"),
        ("Obrigado pelo suporte", "Improdutivo"),
        ("Problema com meu pedido", "Produtivo"),
        ("@cliente #pedido 123!!!", "Produtivo"),  # depende das regras do mock
        ("", "Produtivo"),  # texto vazio
    ]
)
def test_classify_text_cases(text, expected_category):
    response = client.post("/api/v1/text", json={"content": text})
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == expected_category
    assert "response" in data

def test_classify_text_missing_field():
    response = client.post("/api/v1/text", json={})
    assert response.status_code == 422  # erro de validação Pydantic
