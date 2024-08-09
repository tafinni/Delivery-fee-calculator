import logging

from fastapi import FastAPI

from app.classes import CartInfo
from app.validation import validate_values
from app.checks import run_extra_fee_checks


LOG_FILE = "events.log"

logging.basicConfig (
	filename = LOG_FILE,
	level = logging.DEBUG,
	encoding = "utf-8",
	format = "%(asctime)s - %(levelname)s : %(message)s"
)

app = FastAPI(title="Calculator API")

@app.on_event("startup")
async def startup_event():
	logging.FileHandler(LOG_FILE, "w")


@app.post("/calculate-delivery-fee")
async def calculate_delivery_fee(data: CartInfo):
	cart_value_for_free_delivery = 20000
	maximum_delivery_fee = 1500

	# Validating input
	validate_values(data)

	# Check if cart_value qualifies for free delivery
	if data.cart_value >= cart_value_for_free_delivery:
		logging.info("Cart value is equal or more to free delivery amount")
		return {"delivery_fee": 0}
	
	# Checking and calculating possible extra fees and adding them together
	delivery_fee = run_extra_fee_checks(data)

	# Check if delivery_fee is over maximum allowed amount, set delivery_fee lower if necessary
	if delivery_fee > maximum_delivery_fee:
		delivery_fee = maximum_delivery_fee
		logging.info("Delivery fee was more than allowed, changed to maximum allowed value")
	
	return {"delivery_fee": int(delivery_fee)}

