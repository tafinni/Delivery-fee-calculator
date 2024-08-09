import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# --- Tests for cart_value ---

def test_0(): # qualifies for free delivery
	logging.info("\n\n--- TESTING CART_VALUE ---")
	logging.info("\n\ncart_value test_0")
	data = {
		"cart_value": 20000,
		"delivery_distance": 2235,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 0}


def test_1(): # cart_value is 0
	logging.info("\n\ncart_value test_1")
	data = {
		"cart_value": 0,
		"delivery_distance": 2235,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 1500}


def test_2(): # cart_value is negative
	logging.info("\n\ncart_value test_2")
	data = {
		"cart_value": -10,
		"delivery_distance": 2235,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid cart_value: has to be positive value and not larger than given maximum value"}


def test_3(): # cart_value is very high number
	logging.info("\n\ncart_value test_3")
	data = {
		"cart_value": 9999999999999999999999999999999999999999,
		"delivery_distance": 2235,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid cart_value: has to be positive value and not larger than given maximum value"}


def test_4(): # value just below required minimum cart_value
	logging.info("\n\ncart_value test_4")
	data = {
		"cart_value": 999,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 201}


def test_5(): # value exactly minimum required cart_Value
	logging.info("\n\ncart_value test_5")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 200}

