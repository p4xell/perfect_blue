from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *

menu = [
    {'title': 'Главная', 'url': 'main'},
    {'title': 'Хит продаж', 'url': 'bestseller'},
    {'title': 'Корзина', 'ulr': 'basket'},
    {'title': 'Профиль', 'url': 'profile'}
]

cats = Categories.objects.all()


class AllFlowers(ListView):
    model = Flowers
    template_name = 'flowers/base.html'
    context_object_name = 'flowers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['categories'] = cats
        return context
