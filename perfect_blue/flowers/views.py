from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, ListView, DetailView, CreateView

from .forms import RegisterUserForm
from .models import Categories, Flowers
from cart.forms import CartAddProductForm

from .utils import DataMixin, menu, cats


class Main(DataMixin, ListView):
    model = Flowers
    template_name = 'flowers/main.html'
    context_object_name = 'flowers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context()
        return dict(list(context.items()) + list(user_context.items()))


class CategoriesFlowers(DataMixin, ListView):
    model = Flowers
    template_name = 'flowers/main.html'
    context_object_name = 'flowers'

    def get_queryset(self):
        return Flowers.objects.filter(cat__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context()
        return dict(list(context.items()) + list(user_context.items()))


class PostFlowers(DataMixin, View):
    def get(self, request, post_slug):
        post = Flowers.objects.get(slug=post_slug)
        cart_product_form = CartAddProductForm()
        context = {
            'menu': menu,
            'categories': cats,
            'post': post,
            'cart_product_form': cart_product_form,
        }

        return render(request, 'flowers/post.html', context)

    def post(self, request, post_slug):
        post = Flowers.objects.get(slug=post_slug)
        post.number_of_purchases += 1
        post.save()
        context = {
            'menu': menu,
            'categories': cats,
            'post': post
        }
        return render(request, 'flowers/post.html', context)


class BestSeller(View):
    def get(self, request):
        flowers = []
        for item in Flowers.objects.all():
            flowers.append(item)
        number_of_purchases_lst = []
        for i in range(3):
            index = 0
            max_value = 0
            for f in range(len(flowers)):
                if flowers[f].number_of_purchases > max_value:
                    max_value = flowers[f].number_of_purchases
                    index = f

            number_of_purchases_lst.append(flowers[index])
            del flowers[index]

        context = {
            'menu': menu,
            'categories': cats,
            'flowers': number_of_purchases_lst,
        }
        return render(request, 'flowers/bestseller.html', context)


def cart(request):
    return HttpResponse('cart')


class Profile(View):
    def get(self, request):
        return render(request, 'flowers/profile.html', {'menu': menu})

    def post(self, request):
        logout(request)
        return redirect('main')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'flowers/registration.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(menu=menu)
        return dict(list(context.items()) + list(user_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        redirect('main')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'flowers/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(menu=menu)
        return dict(list(context.items()) + list(user_context.items()))
