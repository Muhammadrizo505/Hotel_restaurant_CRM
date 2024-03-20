from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

"""  GET API """
class GetHotel(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class GetRestaurant(ListAPIView):
    queryset = Restouran.objects.all()
    serializer_class = RestauranSerializer


class GetRating(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class GetEmployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class GetFoodOrder(ListAPIView):
    queryset = Order_food.objects.all()
    serializer_class = FoodOrderSerializer




class GetFoodCategory(ListAPIView):
    queryset = Food_category.objects.all()
    serializer_class = FoodcategorySerializer


class GetAddress(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class GetMenu(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class GetOrder(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

"""  Filter  """
@api_view(["GET"])
def hotel_by_name(request):
    name = request.GET.get("name")
    hotel = Hotel.objects.filter(name = name)
    ser = HotelSerializer(hotel, many=True)
    return Response(ser.data)

@api_view(["GET"])
def hotel_by_location(request):
    location = request.GET.get("location")
    hotel = Hotel.objects.filter(location = location)
    ser = HotelSerializer(hotel)
    return Response(ser.data)

@api_view(["GET"])
def hotel_by_contact(request):
    contact = request.GET.get("contact")
    hotel = Hotel.objects.filter(contact = contact)
    ser = HotelSerializer(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def restouran_by_name(request):
    name = request.GET.get('name')
    restorant = Restouran.objects.filter(name = name)
    ser = RestauranSerializer(restorant, many=True)
    return  Response(ser.data)


@api_view(['GET'])
def restouran_by_location(request):
    location = request.GET.get('location')
    restorant = Restouran.objects.filter(name = name)
    ser = RestauranSerializer(restorant)
    return  Response(ser.data)


@api_view(["GET"])
def restouran_by_contact(request):
    contact = request.GET.get("contact")
    restouran = Restouran.objects.filter(contact = contact)
    ser = RestouranSerializer(hotel, many=True)
    return Response(ser.data)



@api_view(["GET"])
def employee_by_firstname(request):
    firstname = request.GET.get("first_name")
    employee = Employee.objects.filter(contact = contact)
    ser = EmployeeSerializer(hotel, many=True)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_lastname(request):
    lastname = request.GET.get("last_name")
    employee = Employee.objects.filter(contact = contact)
    ser = EmployeeSerializer(hotel, many=True)
    return Response(ser.data)



@api_view(["GET"])
def employee_by_phone_number(request):
    phone_number = request.GET.get("phone_number")
    employee = Employee.objects.filter(contact = contact)
    ser = EmployeeSerializer(hotel, many=True)
    return Response(ser.data)

@api_view(["GET"])
def employee_by_rating(request):
    rating = request.GET.get("rating")
    employee = Employee.objects.filter(rating = rating)
    ser = EmployeeSerializer(hotel, many=True)
    return Response(ser.data)




@api_view(["GET"])
def order_by_name(request):
    name = request.GET.get("name")
    order = Order.objects.filter(name = name)
    ser = OrderSerializer(hotel, many=True)
    return Response(ser.data)


@api_view(["GET"])
def order_by_room(request):
    room = request.GET.get("room")
    order = Order.objects.filter(room = room)
    ser = OrderSerializer(hotel, many=True)
    return Response(ser.data)


@api_view(["GET"])
def food_order_by_name(request):
    name = request.GET.get("name")
    order = Order_food.objects.filter(name = name)
    ser = FoodOrderSerializer(hotel, many=True)
    return Response(ser.data)

@api_view(["GET"])
def food_order_by_food(request):
    food = request.GET.get("food")
    order = Order_food.objects.filter(food = food)
    ser = FoodOrderSerializer(hotel, many=True)
    return Response(ser.data)


@api_view(["GET"])
def food_order_by_isdeliver(request):
    isdeliver = request.GET.get("isdeliver")
    order = Order_food.objects.filter(isdeliver = isdeliver)
    ser = FoodOrderSerializer(hotel, many=True)
    return Response(ser.data)

@api_view(["GET"])
def food_order_by_phone_number(request):
    phone_number = request.GET.get("phone_number")
    order = Order_food.objects.filter(phone_number = phone_number)
    ser = FoodOrderSerializer(hotel, many=True)
    return Response(ser.data)