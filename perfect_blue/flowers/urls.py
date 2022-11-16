from django.urls import path
from .views import *


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('bestseller/', bestseller, name='bestseller'),
    path('basket/', basket, name='basket'),
    path('profile/', profile, name='profile'),
    path('post/<slug:post_slug>/', PostFlowers.as_view(), name='post'),
    path('category/<slug:category_slug>/', CategoriesFlowers.as_view(), name='category'),

]
