from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root_should_return_200():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Facebook API"}
    

# def test_invalid_id_should_return_404():
#     response = client.get("/posts/99")
#     assert response.status_code == 404
    
    
    
def test_noninteger_id_should_return_422():
    response = client.get("/posts/abc")
    assert response.status_code == 422