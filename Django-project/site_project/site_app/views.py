from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse, reverse_lazy
from site_app.forms import CategoryForm, ProductForm
from site_app.models import Product, Category


class IndexView(TemplateView):
    template_name = "site_app/index.html"


class CategoryView(ListView):
    model = Category
    template_name = "site_app/categories.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "site_app/categories_detail.html"
    context_object_name = 'category_detail'


class CategoryAddView(CreateView):
    model = Category
    template_name = "site_app/categories_add.html"
    form_class = CategoryForm


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "site_app/categories_confirm_delete.html"
    success_url = reverse_lazy("site_app:ListCategory")
    context_object_name = "category_delete"


class ArticleList(ListView):
    model = Product
    template_name = "site_app/article.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Product
    template_name = "site_app/article_detail.html"
    context_object_name = "article_detail"
