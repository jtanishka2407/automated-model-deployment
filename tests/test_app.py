import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Iris Flower Prediction" in response.data

def test_predict_route():
    client = app.test_client()
    sample_input = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200

    data = response.get_json()
    assert "prediction" in data
    assert data["prediction"] in [0, 1, 2]
