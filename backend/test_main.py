from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Servidor de Recetas IA activo"}

def test_buscar_receta():
    # Probamos que el endpoint responda
    response = client.get("/buscar?ingredientes=huevo")
    assert response.status_code == 200
    assert "receta" in response.json()