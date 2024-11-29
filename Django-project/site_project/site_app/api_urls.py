from django.urls import path
from rest_framework.routers import DefaultRouter

from . import api_views
from .api_views import (
    CategoryTopListAPIView,
    CategoryDetailAPIView, ProductCreatorViewSet, )

app_name = 'site_app_api'

router = DefaultRouter()
router.register(
    prefix=r"categories",
    viewset=api_views.CategoryViewSet,
    basename="category",
)

router.register(
    prefix=r"products",
    viewset=api_views.ProductViewSet,
    basename="product",
)

router.register(
    prefix=r'filter_products',
    viewset=api_views.FilteringProductViewSet,
    basename="filter-product",
)

urlpatterns = [
    path(
        "top-categories/",
        CategoryTopListAPIView.as_view(),
        name="top-categories"
    ),
    path(
        "min-categories/<int:pk>/",
        CategoryDetailAPIView.as_view(),
        name="min-category-details"
    ),
    path('creatorarticles/<int:user_id>/', ProductCreatorViewSet.as_view({'get': 'list'}), name='articles-list'),
    *router.urls,
]
