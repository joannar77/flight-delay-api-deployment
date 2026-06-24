from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is functional"}

def test_predict_invalid_airport():
    response = client.get(
        "/predict/delays",
        params={
            "arrival_airport": "ZZZ",
            "dep_time": 1400,
            "arr_time": 1630
        }
    )
    assert response.status_code == 200
    assert response.json() == {"error": "Airport not recognized"}

def test_predict_request_shape():
    response = client.get(
        "/predict/delays",
        params={
            "arrival_airport": "LAX",
            "dep_time": 1400,
            "arr_time": 1630
        }
    )
    assert response.status_code == 200

def test_missing_parameter():
    response = client.get(
        "/predict/delays",
        params={
            "arrival_airport": "LAX",
            "dep_time": 1400
            # arr_time missing
        }
    )
    assert response.status_code == 422