import logging

from fastapi import HTTPException

from datetime import datetime
from app.classes import CartInfo


def validate_values(data: CartInfo):
	max_cart_value = 10000000
	max_delivery_distance = 100000
	max_number_of_items = 1000

	# Validate cart_value
	if data.cart_value < 0 or data.cart_value > max_cart_value:
		error_msg = "Invalid cart_value: has to be positive value and not larger than given maximum value"
		logging.error(error_msg)
		raise HTTPException(status_code=400, detail=error_msg)
	
	# Validate delivery_distance
	if data.delivery_distance < 0 or data.delivery_distance > max_delivery_distance:
		error_msg = "Invalid delivery_distance: has to be positive value and not larger than given maximum value"
		logging.error(error_msg)
		raise HTTPException(status_code=400, detail=error_msg)
	
	# Validate number_of_items
	if data.number_of_items <= 0 or data.number_of_items > max_number_of_items:
		error_msg = "Invalid number_of_items: has to be a postitive value above zero and not larger than given maximum value"
		logging.error(error_msg)
		raise HTTPException(status_code=400, detail=error_msg)

	# Validate time
	try:
		datetime.strptime(data.time, "%Y-%m-%dT%H:%M:%SZ")
	except ValueError:
		error_msg = "Invalid UTC: has to be in format YYY-MM-DDTHH:MM:SSZ"
		logging.exception(error_msg)
		raise HTTPException(status_code=400, detail=error_msg)
	
	logging.info("Values validated succesfully")

