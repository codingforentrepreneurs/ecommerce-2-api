from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.detail import DetailView
from  django.views.generic.list import ListView
# Create your views here.


from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView



from .forms import AddressForm, UserAddressForm
from .mixins import CartOrderMixin, LoginRequiredMixin
from .models import UserAddress, UserCheckout, Order

User = get_user_model()

class UserCheckoutMixin(object):

	def user_failure(self, message=None):
		data = {
			"message": "There was an error. Please try again",
			"success": False
		}
		if message:
			data["message"] = message
		return data


	def get_checkout_data(self, user=None, email=None):
		if email and not user:
			user_exists = User.objects.filter(email=email).count()
			if user_exists != 0:
				return self.user_failure(message="This user already exists, please login.")

		data = {}
		if user and not email:
			if user.is_authenticated():
				user_checkout = UserCheckout.objects.get_or_create(user=user, email=user.email)[0] #(instance, created)
				data["token"] = user_checkout.get_client_token()
				data["braintree_id"] = user_checkout.get_braintree_id
				data["user_checkout_id"] = user_checkout.id
			else:
				#return error
				pass
		elif not user and email:
			user_checkout = UserCheckout.objects.get_or_create(email=email)[0] #(instance, created)
			
		elif user and email:
			user_checkout = False
		else:
			user_checkout = False

		if user_checkout:
			data["token"] = user_checkout.get_client_token()
			data["braintree_id"] = user_checkout.get_braintree_id
			data["user_checkout_id"] = user_checkout.id
			data["success"]= True

		return data


class UserCheckoutAPI(UserCheckoutMixin, APIView):
	permission_classes = [AllowAny]
	def get(self, request, format=None):
		data = self.get_checkout_data(user=request.user)
		return Response(data)

	def post(self, request, format=None):
		data = {}
		email = request.data.get("email")
		if email:
			data = self.get_checkout_data(email=email)
		return Response(data)




class OrderDetail(DetailView):
	model = Order

	def dispatch(self, request, *args, **kwargs):
		try:
			user_check_id = self.request.session.get("user_checkout_id")
			user_checkout = UserCheckout.objects.get(id=user_check_id)
		except UserCheckout.DoesNotExist:
			user_checkout = UserCheckout.objects.get(user=request.user)
		except:
			user_checkout = None

		obj = self.get_object()
		if obj.user == user_checkout and user_checkout is not None:
			return super(OrderDetail, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404




class OrderList(LoginRequiredMixin, ListView):
	queryset = Order.objects.all()

	def get_queryset(self):
		user_check_id = self.request.user.id
		user_checkout = UserCheckout.objects.get(id=user_check_id)
		return super(OrderList, self).get_queryset().filter(user=user_checkout)




class UserAddressCreateView(CreateView):
	form_class = UserAddressForm
	template_name = "forms.html"
	success_url = "/checkout/address/"

	def get_checkout_user(self):
		user_check_id = self.request.session.get("user_checkout_id")
		user_checkout = UserCheckout.objects.get(id=user_check_id)
		return user_checkout

	def form_valid(self, form, *args, **kwargs):
		form.instance.user = self.get_checkout_user()
		return super(UserAddressCreateView, self).form_valid(form, *args, **kwargs)



class AddressSelectFormView(CartOrderMixin, FormView):
	form_class = AddressForm
	template_name = "orders/address_select.html"


	def dispatch(self, *args, **kwargs):
		b_address, s_address = self.get_addresses()
		if b_address.count() == 0:
			messages.success(self.request, "Please add a billing address before continuing")
			return redirect("user_address_create")
		elif s_address.count() == 0:
			messages.success(self.request, "Please add a shipping address before continuing")
			return redirect("user_address_create")
		else:
			return super(AddressSelectFormView, self).dispatch(*args, **kwargs)


	def get_addresses(self, *args, **kwargs):
		user_check_id = self.request.session.get("user_checkout_id")
		user_checkout = UserCheckout.objects.get(id=user_check_id)
		b_address = UserAddress.objects.filter(
				user=user_checkout,
				type='billing',
			)
		s_address = UserAddress.objects.filter(
				user=user_checkout,
				type='shipping',
			)
		return b_address, s_address


	def get_form(self, *args, **kwargs):
		form = super(AddressSelectFormView, self).get_form(*args, **kwargs)
		b_address, s_address = self.get_addresses()

		form.fields["billing_address"].queryset = b_address
		form.fields["shipping_address"].queryset = s_address
		return form

	def form_valid(self, form, *args, **kwargs):
		billing_address = form.cleaned_data["billing_address"]
		shipping_address = form.cleaned_data["shipping_address"]
		order = self.get_order()
		order.billing_address = billing_address
		order.shipping_address = shipping_address
		order.save()
		return  super(AddressSelectFormView, self).form_valid(form, *args, **kwargs)

	def get_success_url(self, *args, **kwargs):
		return "/checkout/"