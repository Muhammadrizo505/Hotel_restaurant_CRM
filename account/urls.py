from django.urls import path
from .views import *


urlpatterns = [
    path('sign_up/', sing_up_view),
    path('sign_in/', singin_view),
]