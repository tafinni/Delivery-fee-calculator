import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# --- Tests for number_of_items ---

def test_0(): # Test items under extra fee amount
	logging.info("\n\n--- TESTING NUMBER_OF_ITEMS ---")
	logging.info("\n\nnumber_of_items test_0")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 200}


def test_1(): # Test no items
	logging.info("\n\nnumber_of_items test_1")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 0,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid number_of_items: has to be a postitive value above zero and not larger than given maximum value"}


def test_2(): # Test negative items
	logging.info("\n\nnumber_of_items test_2")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": -5,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid number_of_items: has to be a postitive value above zero and not larger than given maximum value"}


def test_3(): # Test items requiring extra fee
	logging.info("\n\nnumber_of_items test_3")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 5,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 250}


def test_4(): # Test items requiring extra + bulk fees
	logging.info("\n\nnumber_of_items test_4")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 13,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 770}


def test_5(): # Test very large amount of items
	logging.info("\n\nnumber_of_items test_5")
	data = {
		"cart_value": 1000,
		"delivery_distance": 1000,
		"number_of_items": 999999999999999999999999,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 400
	assert response.json() == {"detail":"Invalid number_of_items: has to be a postitive value above zero and not larger than given maximum value"}

