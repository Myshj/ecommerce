from rest_framework import serializers
from django.contrib.auth.models import User
from models import Product, Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'title', 'description', 'slug', 'featured')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'title', 'description', 'category')
