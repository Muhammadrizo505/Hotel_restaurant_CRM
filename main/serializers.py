from .models import *
from account.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = User
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Employee
        fields = "__all__"

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Hotel
        fields = "__all__"


class RestauranSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Restorant
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Address
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Order
        fields = "__all__"





class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Rating
        fields = "__all__"


class FoodcategorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Food_category
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Menu
        fields = "__all__"


class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Order_food
        fields = "__all__"
















