from rest_framework import serializers



from products.models import Variation

from .models import CartItem



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









