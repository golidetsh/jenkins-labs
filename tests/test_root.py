from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Facebook API"}
    

def test_invalid_id():
    response = client.get("/posts/99")
    assert response.status_code == 404
    assert response.json() == {'detail': 'id not found'}