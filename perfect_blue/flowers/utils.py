from .models import Flowers, Categories

menu = [
    {'title': 'Главная', 'url': 'main'},
    {'title': 'Хит продаж', 'url': 'bestseller'},
]
cats = Categories.objects.all()


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['categories'] = cats
        return context
