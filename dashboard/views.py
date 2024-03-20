from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from main.models import *
from main.serializers import *


class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer






class CreateHotel(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class UpdateHotel(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class DeleteHotel(DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer




class CreateRestorant(ListCreateAPIView):
    queryset = Restouran.objects.all()
    serializer_class = RestauranSerializer


class UpdateRestorant(UpdateAPIView):
    queryset = Restouran.objects.all()
    serializer_class = RestauranSerializer


class DeleteRestorant(DestroyAPIView):
    queryset = Restouran.objects.all()
    serializer_class = RestauranSerializer





class CreateAddress(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UpdateAddress(UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class DeleteAddress(DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer






class CreateOrder(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UpdateOrder(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeleteOrder(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer





class CreateFoodOrder(ListCreateAPIView):
    queryset = Order_food.objects.all()
    serializer_class = FoodOrderSerializer

class UpdateFoodOrder(UpdateAPIView):
    queryset = Order_food.objects.all()
    serializer_class = FoodOrderSerializer

class DeleteFoodOrder(DestroyAPIView):
    queryset = Order_food.objects.all()
    serializer_class = FoodOrderSerializer





class CreateMenu(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class UpdateMenu(UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class DeleteMenu(DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer





class CreateRating(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class UpdateRating(UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class DeleteRating(DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer






class CreateFoodCategory(ListCreateAPIView):
    queryset = Food_category.objects.all()
    serializer_class = FoodcategorySerializer


class UpdateFoodCategory(UpdateAPIView):
    queryset = Food_category.objects.all()
    serializer_class = FoodcategorySerializer


class DeleteFoodCategory(DestroyAPIView):
    queryset = Food_category.objects.all()
    serializer_class = FoodcategorySerializer





