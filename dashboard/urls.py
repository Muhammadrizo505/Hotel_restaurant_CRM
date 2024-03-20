from django.urls import path
from .views import *


urlpatterns = [
 path('create-employee', CreateEmployee.as_view()),
 path('update-employee/<int:pk>/', UpdateEmployee.as_view()),
 path('delete-employee/<int:pk>/', DeleteEmployee.as_view()),


 path('create-hotel/', CreateHotel.as_view()),
 path('update-hotel/<int:pk>/', UpdateHotel.as_view()),
 path('delete-hotel/<int:pk>/', DeleteHotel.as_view()),


 path('create-restoran/', CreateRestorant.as_view()),
 path('update-restoran/<int:pk>/', UpdateRestorant.as_view()),
 path('delete-restoran/<int:pk>/', DeleteRestorant.as_view()),


 path('create-address/', CreateAddress.as_view()),
 path('update-address/<int:pk>/', UpdateAddress.as_view()),
 path('delete-address/<int:pk>/', DeleteAddress.as_view()),


 path('create-category/', CreateFoodCategory.as_view()),
 path('update-category/<int:pk>/', UpdateFoodCategory.as_view()),
 path('delete-category/<int:pk>/', DeleteFoodCategory.as_view()),


 path('create-order/', CreateOrder.as_view()),
 path('update-order/<int:pk>/', UpdateOrder.as_view()),
 path('delete-order/<int:pk>/', DeleteOrder.as_view()),


 path('create-rating/', CreateRating.as_view()),
 path('update-rating/<int:pk>/', UpdateRating.as_view()),
 path('delete-rating/<int:pk>/', DeleteRating.as_view()),

 path('create-menu/', CreateMenu.as_view()),
 path('update-menu/<int:pk>/', UpdateMenu.as_view()),
 path('delete-menu/<int:pk>/', DeleteMenu.as_view()),


 path('create-food-order/', CreateFoodOrder.as_view()),
 path('update-food-order/<int:pk>/', UpdateFoodOrder.as_view()),
 path('delete-food-order/<int:pk>/', DeleteFoodOrder.as_view()),


 ]