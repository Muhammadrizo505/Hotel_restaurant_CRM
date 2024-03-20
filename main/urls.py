from django.urls import path
from .views import *


urlpatterns = [
    path('get_hotel', GetHotel.as_view()),
    path('get_restaurant', GetRestaurant.as_view()),
    path('get_rating', GetRating.as_view()),
    path('get_employee',  GetEmployee.as_view()),
    path('get_food_order', GetFoodOrder.as_view()),
    path('get-category', GetFoodCategory.as_view()),
    path('get_address', GetAddress.as_view()),
    path('get_menu', GetMenu.as_view()),
    path('get_order', GetOrder.as_view()),


    path('fiter-hotel_by_name', hotel_by_name),
    path('fiter-hotel_by_lcation', hotel_by_location),
    path('fiter-hotel_by_contact', hotel_by_contact),

    path('filter-restouran_by_name', restouran_by_name),
    path('filter-restouran_by_location', restouran_by_location),
    path('filter-restouran_by_contact', restouran_by_contact),

    path('filter-employee_by_firstname',employee_by_firstname ),
    path('filter-employee_by_lastname',employee_by_lastname ),
    path('filter-employee_by_phone_number',employee_by_phone_number ),
    path('filter-employee_by_rating',employee_by_rating ),

    path('filter-order_by_name',order_by_name),
    path('filter-order_by_room',order_by_room),
    path('filter-order_by_room',order_by_room),

    path('filter-food_order_by_name',food_order_by_name),
    path('filter-food_order_by_food',food_order_by_food),
    path('filter-food_order_by_isdeliver',food_order_by_isdeliver),
    path('filter-food_order_by_phone_number',food_order_by_phone_number),


]