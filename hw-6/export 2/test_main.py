import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_chat_completions():
    response = client.post("/v1/chat/completions", json={"messages": [{"role": "user", "content": "Hola"}]})
    assert response.status_code == 200
    data = response.json()
    assert "choices" in data
    assert data["choices"][0]["message"]["content"] == "Hola, soy un mock!" 