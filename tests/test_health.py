from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_should_returns_200():
    client = TestClient(app)

    response = client.get('/api/health')

    assert response.status_code == 200
    assert response.json() == {'message': 'OK'}
