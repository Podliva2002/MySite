from rest_framework import serializers

from site_app.models import Category, Product


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
