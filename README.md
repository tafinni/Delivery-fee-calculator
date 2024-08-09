# Delivery-fee-calculator
Delivery fee calculator done for internship application at Wolt.
It calculates the delivery fee based on cart value, delivery distance, number of items, and time of order.

Calculator works by recieving json of this type:
```
{
		"cart_value": int,
		"delivery_distance": int,
		"number_of_items": int,
		"time": "YYYY-MM-DDTHH:MM:SSZ"
}
```

**How to run**

1. Create enviroment:
- python -m venv .venv

2. Activate with:
- source .venv/bin/activate

3. Install requirements
- pip install -r requirements.txt

4. Run app
- uvicorn app.main:app --reload

5. Trying it out
- If you have FastAPI go to http://127.0.0.1:8000/docs
- Or try with curl command:
  - curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}' http://127.0.0.1:8000/calculate-delivery-fee

6. Run tests from tests/
-pytest -W tests/

  
