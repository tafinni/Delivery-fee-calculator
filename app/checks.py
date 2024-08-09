import logging

from datetime import datetime, time
from app.classes import CartInfo, Days


def run_extra_fee_checks(data: CartInfo) -> int:
	rush_hour_counter = 1.2

	sub_fee = check_cart_value(data.cart_value)
	distance_fee = check_delivery_distance(data.delivery_distance)
	item_count_fee = check_item_count(data.number_of_items)
	delivery_fee = sub_fee + distance_fee + item_count_fee

	# Check if order is placed during Friday rush and calculate possible extra fee
	if check_rush_time(data.time):
		delivery_fee = delivery_fee * rush_hour_counter
		logging.info("Order is placed during Friday rush")
	return delivery_fee


def check_cart_value(current_value: int) -> int:
	minimum_cart_value = 1000

	if current_value < minimum_cart_value:
		logging.info("Cart value requires extra fee")
		return minimum_cart_value - current_value
	logging.info("Cart value not requiring extra fee")
	return 0
	

def check_delivery_distance(distance: int) -> int:
	default_fee = 200
	extra_fee = 100
	default_delivery_distance = 1000
	distance_for_extra_fee = 500

	if distance <= default_delivery_distance:
		logging.info("Delivery distance not requiring extra fee")
		return default_fee
	
	fee_counter = ((distance - default_delivery_distance) / distance_for_extra_fee)
	if fee_counter % 1 > 0:
		fee_counter += 1

	distance_fee = (int(fee_counter) * extra_fee) + default_fee
	logging.info("Delivery distance requires extra fee")
	return distance_fee


def check_item_count(items: int) -> int:
	item_count_fee = 0
	bulk_item_amount = 13
	extra_fee_item_amout = 5
	extra_fee_for_item = 50
	bulk_extra_fee = 120

	if items < extra_fee_item_amout:
		logging.info("Number of items not requiring extra fee")
		return item_count_fee
	
	item_count_fee = (items - (extra_fee_item_amout - 1)) * extra_fee_for_item
	if items >= bulk_item_amount:
		item_count_fee += bulk_extra_fee
	logging.info("Number of items require extra fee")
	return item_count_fee


def check_rush_time(order_time: str) -> bool:
	rush_day = Days.FRIDAY.value
	rush_start = time(15, 0, 0)
	rush_end = time(18, 59, 59)

	date = datetime.strptime(order_time, "%Y-%m-%dT%H:%M:%SZ")
	if date.weekday() == rush_day:
		if rush_start <= date.time() <= rush_end:
			return True
	return False

