from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('<slug:flower_slug>/', ShowFlowers.as_view(), name='flowers'),

]
