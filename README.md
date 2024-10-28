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

1. Make sure your device has Docker installed. If not, you can get it from the official Docker website.

2. Build the docker image, this will run tests with pytest before production image
	```
	docker build -t delivery-fee-calculator .
	```

3. Run container
	```
	docker run -p 8000:8000 --name delivery-fee-calculator delivery-fee-calculator
	```
4. Try the calculator
   - Navigate to http://localhost:8000/docs and test the calculator with different values
   - Optionally test the calculator with curl command, example:
		```
   		curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}' http://localhost:8000/calculate-delivery-fee
   		```
5. How to find and read events.log:
   - Access container
		```
 		docker exec -it delivery-fee-calculator /bin/bash
 		```
   - Read events.log
		```
   		cat events.log
   		```
   - Exit container view
		```
   		exit
  		```

6.  Close app with ctrl + C if it is open in terminal, or
	```
 	docker stop delivery-fee-calculator
 	```    

  
