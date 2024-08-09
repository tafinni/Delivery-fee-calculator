import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# --- Tests for time ---

def test_0(): # Test invalid time, wrong format
	logging.info("\n\n--- TESTING TIME ---")
	logging.info("\n\ntime test_0")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid UTC: has to be in format YYY-MM-DDTHH:MM:SSZ"}


def test_1(): # Test invalid time, not existing hour
	logging.info("\n\ntime test_1")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-15T36:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid UTC: has to be in format YYY-MM-DDTHH:MM:SSZ"}


def test_2(): # Test friday rush
	logging.info("\n\ntime test_2")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-26T17:43:12Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 240}


def test_3(): # Test time second before friday rush
	logging.info("\n\ntime test_3")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-26T14:59:59Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 200}


def test_4(): # Test time at first second of friday rush
	logging.info("\n\ntime test_4")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-26T15:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 240}


def test_5(): # Test time at last second of friday rush
	logging.info("\n\ntime test_5")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-26T18:59:59Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 240}


def test_6(): # Test time second after friday rush
	logging.info("\n\ntime test_6")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-26T19:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 200}

	