import textwrap

from django.contrib import admin
from .models import Category, Product, Contact


class CategoryInline(admin.TabularInline):
    model = Product.category.through


class ProductInline(admin.TabularInline):
    model = Category.products.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = 'pk', 'name'
    list_display_links = "pk", "name"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    list_display = 'pk', 'name', 'author', 'category_list', 'description_short'
    list_display_links = "pk", "name"

    @staticmethod
    def description_short(obj: Product) -> str:
        return textwrap.shorten(obj.description, width=60)

    @staticmethod
    def category_list(obj: Product) -> str:
        return ", ".join([c.name for c in obj.category.all()])


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'email'
    list_display_links = "pk", "name", 'email'

