from django.urls import path
from .views import *

urlpatterns = [
    path('', AllFlowers.as_view(), name='all_flowers')

]