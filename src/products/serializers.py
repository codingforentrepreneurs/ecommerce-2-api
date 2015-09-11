from rest_framework import serializers


from .models import Category



class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = [
			"url",
			"id",
			"title",
			"description",

		]



#CREATE RETRIEVE UPDATE DESTROY