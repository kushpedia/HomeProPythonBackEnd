from rest_framework import serializers
from category.models import Category
from service.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)  # Include related services

    class Meta:
        model = Category
        fields = '__all__'