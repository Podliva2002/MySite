from django.contrib.auth.models import User
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, pagination
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategoryMinimalSerializer, CategoryDetailSerializer, ProductSerializer, CategorySerializer, \
    ProductSerializerCreate, UserSerializer


class CategoryTopListAPIView(ListAPIView):
    queryset = Category.objects.all()[:5]
    serializer_class = CategoryMinimalSerializer


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreatorViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Product.objects.filter(author=user_id)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })


class TimezonePagination(pagination.PageNumberPagination):
    page_size = 5

    def get_paginated_response(self, data):
        from rest_framework.response import Response
        return Response({
            'current_time': timezone.now(),
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class FilteringProductViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()

    permission_classes = [AllowAny]
    pagination_class = TimezonePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'complexity']

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductSerializerCreate
        return ProductSerializer

    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     product = self.get_object()
    #     result = product.price > 100
    #     return Response({'status': result})
