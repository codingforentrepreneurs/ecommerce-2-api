from rest_framework import serializers



from products.models import Variation

from .models import CartItem


"""

{
"cart_token": "12345", 
"billing_address": 1,
"shipping_address": 1,
"checkout_token": "12345",
}

"""
class CheckoutSerializer(serializers.Serializer):
	checkout_token = serializers.CharField()
	user_checkout_id =serializers.IntegerField(required=False)
	billing_address = serializers.IntegerField()
	shipping_address = serializers.IntegerField()
	cart_token = serializers.CharField()
	cart_id = serializers.IntegerField(required=False)


	def validate_checkout_token(self, value):
		print type(value)
		if type(value) == type(str()):
			return value
		raise serializers.ValidationError("This is not a valid token.")



class CartVariationSerializer(serializers.ModelSerializer):
	product = serializers.SerializerMethodField()
	class Meta:
		model = Variation
		fields = [
			"id",
			"title",
			"price",
			"product",
		]

	def get_product(self, obj):
		return obj.product.title



class CartItemSerializer(serializers.ModelSerializer):
	#item = CartVariationSerializer(read_only=True)
	item = serializers.SerializerMethodField()
	item_title = serializers.SerializerMethodField()
	product = serializers.SerializerMethodField()
	price = serializers.SerializerMethodField()
	class Meta:
		model = CartItem
		fields = [
			"item",
			"item_title",
			"price",
			"product",
			"quantity",
			"line_item_total",
		]

	def get_item(self,obj):
		return obj.item.id
		
	def get_item_title(self, obj):
		return "%s %s" %(obj.item.product.title, obj.item.title)

	def get_product(self, obj):
		return obj.item.product.id

	def get_price(self, obj):
		return obj.item.price









