from django.contrib import admin

from .models import *


class FlowersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'price']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'description']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']


admin.site.register(Flowers, FlowersAdmin)
admin.site.register(Categories, CategoriesAdmin)
