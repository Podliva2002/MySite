from .views import (
    IndexView,
    CategoryView,
    CategoryDetailView,
    ArticleList,
    ArticleDetailView,
    CategoryAddView,
    CategoryDeleteView,
)

from django.urls import path

app_name = 'site_app'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("categories/", CategoryView.as_view(), name="ListCategory"),
    path("categories/add/", CategoryAddView.as_view(), name="category-add"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),
    path("articles/", ArticleList.as_view(), name="ListArticle"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
]
