import textwrap

from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = "pk", "name"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'price', 'category_list', 'description_short'
    list_display_links = "pk", "name"

    @staticmethod
    def description_short(obj: Product) -> str:
        return textwrap.shorten(obj.description, width=60)

    @staticmethod
    def category_list(obj: Product) -> str:
        return ", ".join([c. name for c in obj.category.all()])