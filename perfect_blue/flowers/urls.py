from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('bestseller/', bestseller, name='bestseller'),
    path('basket/', basket, name='basket'),
    path('profile/', profile, name='profile'),
    path('flowers/<slug:flower_slug>/', ShowFlowers.as_view(), name='flowers'),

]
