import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_classify_produtivo():
    response = client.post(
        "/api/v1/classify/",
        json={"text": "Preciso de atualização do meu pedido"}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["category"] == "Produtivo"

def test_classify_improdutivo():
    response = client.post(
        "/api/v1/classify/",
        json={"text": "Feliz Natal para todos!"}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["category"] == "Improdutivo"
