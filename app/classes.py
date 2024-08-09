from pydantic import BaseModel
from enum import Enum


class CartInfo(BaseModel):
	cart_value: int
	delivery_distance: int
	number_of_items: int
	time: str


class Days(Enum):
	MONDAY = 0
	TUESDAY = 1
	WEDNESDAY = 2
	THURSDAY = 3
	FRIDAY = 4
	SATURDAY = 5
	SUNDAY = 6

