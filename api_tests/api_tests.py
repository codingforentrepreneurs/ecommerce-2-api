import requests
import json

cart_url = 'http://127.0.0.1:8000/api/cart/'

def create_cart():
	# create cart
	cart_r = requests.get(cart_url)
	# get cart token
	cart_token = cart_r.json()["token"]
	return cart_token


def do_api_test(email=None, user_auth=None):
	cart_token = create_cart()
	# add items to cart
	new_cart_url = cart_url + "?token=" + cart_token + "&item=10&qty=3"
	new_cart_r = requests.get(new_cart_url)
	#print new_cart_r.text
	#get user_checkout token
	user_checkout_url = 'http://127.0.0.1:8000/api/user/checkout/'
	if email:
		data = {
			"email": email
		}
		u_c_r = requests.post(user_checkout_url, data=data)
		
		user_checkout_token = u_c_r.json().get("user_checkout_token")
		#print user_checkout_token
		addresses = "http://127.0.0.1:8000/api/user/address/?checkout_token=" + user_checkout_token
		#address = "http://127.0.0.1:8000/api/user/address/?checkout_token=eydicmFpbnRyZWVfaWQnOiB1JzY0ODMxMzkzJywgJ3VzZXJfY2hlY2tvdXRfaWQnOiAxMSwgJ3N1Y2Nlc3MnOiBUcnVlfQ=="
		addresses_r = requests.get(addresses)
		addresses_r_data = addresses_r.json()
		if addresses_r_data["count"] >= 2:
			b_id = addresses_r_data["results"][0]["id"]
			s_id = addresses_r_data["results"][1]["id"]
		else:
			addresses_create = "http://127.0.0.1:8000/api/user/address/create/"
			user_id = 11
			data = {
				"user": user_id,
				"type": "billing",
				"street": "12423 Test",
				"city": "Newport Beach",
				"zipcode": 92304,
			}
			addresses_create_r = requests.post(addresses_create, data=data)
			b_id = addresses_create_r.json().get("id")
			data = {
				"user": user_id,
				"type": "shipping",
				"street": "12423 Test",
				"city": "Newport Beach",
				"zipcode": 92304,
			}
			addresses_create_s_r = requests.post(addresses_create, data=data)
			s_id = addresses_create_s_r.json().get("id")
		""" 
		do checkout
		"""
		checkout_url = "http://127.0.0.1:8000/api/checkout/"
		data = {
			"billing_address": b_id,
			"shipping_address": s_id,
			"cart_token": cart_token,
			"checkout_token": user_checkout_token
		}
		#print data
		order = requests.post(checkout_url, data=data)
		#print order.headers
		print order.text



do_api_test(email='abc1234@gmail.com')
















