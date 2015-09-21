
#from orders.models import UserCheckout

def jwt_response_payload_handler(token, user, request, *args, **kwargs):
	data = {
		"token": token,
		"user": user.id,
		#"user_braintree_id": UserCheckout.objects.get(user=user).get_braintree_id
	}
	return data
