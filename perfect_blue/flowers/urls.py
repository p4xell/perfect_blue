from django.urls import path
from .views import *


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('bestseller/', BestSeller.as_view(), name='bestseller'),
    path('cart/', cart, name='cart'),
    path('profile/', Profile.as_view(), name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('post/<slug:post_slug>/', PostFlowers.as_view(), name='post'),
    path('category/<slug:category_slug>/', CategoriesFlowers.as_view(), name='category'),

]
