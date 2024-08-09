import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# --- Tests combinations of different values ---

def test_0(): # Test with values given in git instructions
	logging.info("\n\n--- TESTING DIFFERENT VALUE COMBINATIOS ---")
	logging.info("\n\ncombinations test_0")
	data = {
		"cart_value": 790,
		"delivery_distance": 2235,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 710}


def test_1(): # No data provided
	logging.info("\n\ncombinations test_1")
	data = {

	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 422


def test_2(): # Value missing
	logging.info("\n\n--- TESTING DIFFERENT VALUE COMBINATIOS ---")
	logging.info("\n\ncombinations test_0")
	data = {
		"cart_value": 790,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 422

