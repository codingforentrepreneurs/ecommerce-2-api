from rest_framework import serializers


from .models import Category, Product, Variation


class VariationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Variation
		fields = [
			"id",
			"title",
			"price",
		]



class ProductDetailUpdateSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True, read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"description",
			"price",
			"image",
			"variation_set",
		]

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None

	def create(self, validated_data):
		title = validated_data["title"]
		Product.objects.get(title=title)
		product = Product.objects.create(**validated_data)
		return product

	def update(self, instance, validated_data):
		instance.title = validated_data["title"]
		instance.save()
		return instance
	# def update


class ProductDetailSerializer(serializers.ModelSerializer):
	variation_set = VariationSerializer(many=True, read_only=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"id",
			"title",
			"description",
			"price",
			"image",
			"variation_set",
		]

	def get_image(self, obj):
		return obj.productimage_set.first().image.url




class ProductSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='products_detail_api')
	variation_set = VariationSerializer(many=True)
	image = serializers.SerializerMethodField()
	class Meta:
		model = Product
		fields = [
			"url",
			"id",
			"title",
			"image",
			"variation_set",
		]

	def get_image(self, obj):
		try:
			return obj.productimage_set.first().image.url
		except:
			return None



class CategorySerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='category_detail_api')
	product_set = ProductSerializer(many=True)
	class Meta:
		model = Category
		fields = [
			"url",
			"id",
			"title",
			"description",
			"product_set", ## obj.product_set.all()
			#"default_category",

		]



#CREATE RETRIEVE UPDATE DESTROY