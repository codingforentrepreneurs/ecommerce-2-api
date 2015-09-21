from django.utils import timezone
#from orders.models import UserCheckout

def jwt_response_payload_handler(token, user, request, *args, **kwargs):
	data = {
		"token": token,
		"user": user.id,
		"orig_iat": timezone.now(),
		#"user_braintree_id": UserCheckout.objects.get(user=user).get_braintree_id
	}
	return data
