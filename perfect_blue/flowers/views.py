from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Categories, Flowers

menu = [
    {'title': 'Главная', 'url': 'main'},
    {'title': 'Хит продаж', 'url': 'bestseller'},
    {'title': 'Корзина', 'url': 'basket'},
    {'title': 'Профиль', 'url': 'profile'}
]

cats = Categories.objects.all()


class Main(ListView):
    model = Flowers
    template_name = 'flowers/main.html'
    context_object_name = 'flowers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['categories'] = cats
        return context


class ShowFlowers(ListView):
    model = Flowers
    template_name = 'flowers/main.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        return Flowers.objects.filter(cat__slug=self.kwargs['flower_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['categories'] = cats
        return context


def bestseller(request):
    return HttpResponse('BestSeller')


def basket(request):
    return HttpResponse('basket')


def profile(request):
    return HttpResponse('profile')
