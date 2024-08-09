import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# --- Tests for delivery_distance ---

def test_0(): # Test default delivery fee (delivery_distance 1000 or less)
	logging.info("\n\n--- TESTING DELIVERY_DISTANCE ---")
	logging.info("\n\ndelivery_distance test_0")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 200}


def test_1(): # Test negative delivery_distance
	logging.info("\n\ndelivery_distance test_1")
	data = {
		"cart_value": 1000,
		"delivery_distance": -20000,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid delivery_distance: has to be positive value and not larger than given maximum value"}


def test_2(): # Test delivery_distance that requires extra fee
	logging.info("\n\ndelivery_distance test_2")
	data = {
		"cart_value": 1000,
		"delivery_distance": 4000,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 800}


def test_3(): # Test too large delivery_distance
	logging.info("\n\ndelivery_distance test_3")
	data = {
		"cart_value": 1000,
		"delivery_distance": 99999999999999999999999999999999,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid delivery_distance: has to be positive value and not larger than given maximum value"}
	

def test_4(): # Test delivery_distance just above default fee amount
	logging.info("\n\ndelivery_distance test_4")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1001,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 300}

