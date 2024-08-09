
import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# --- Tests for delivery_fee ---

def test_0(): # Test with big delivery_fee, to make sure it doesn't exceed maximum value
	logging.info("\n\n--- TESTING DELIVERY_FEE ---")
	logging.info("\n\ndelivery_fee test_0")
	data = {
		"cart_value": 200,
		"delivery_distance": 8000,
		"number_of_items": 4,
		"time": "2024-01-15T13:00:00Z"
	}
	response = client.post("/calculate-delivery-fee", json=data)
	assert response.status_code == 200
	assert response.json() == {"delivery_fee": 1500}

	