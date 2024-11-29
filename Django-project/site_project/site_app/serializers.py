from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers

from site_app.models import Category, Product

UserModel = get_user_model()

class CategoryMinimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class CategoryHyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'self'
        )

    self = serializers.HyperlinkedIdentityField(
        view_name='site_app:category-detail',
    )

class AuthorHyperLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'username',
        )



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'category',
            'author',
            'complexity',
        )

    category = CategoryHyperLinkSerializer(
        many=True,
        required=False,
    )

    author = AuthorHyperLinkSerializer(
        many=False,
        required=False,
    )


class ProductSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'category',
            'author',
            'complexity',
        )

    category = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Category.objects.all(),
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)