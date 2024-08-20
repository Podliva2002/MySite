from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
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


class ArticleList(ListView):
    model = Product
    template_name = "site_app/article.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Product
    template_name = "site_app/article_detail.html"
    context_object_name = "article_detail"
