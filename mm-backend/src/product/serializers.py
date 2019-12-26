from rest_framework import serializers

from .models import FirstCategory, AdProduct, Product, Sku


class StringListField(serializers.ListField):
    child = serializers.CharField()


class FirstCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstCategory
        fields = [
            'title',
        ]


class AdProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdProduct
        fields = [
            'location',
            'image',
            'link_url',
        ]


class SkuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = [
            'version',
            'color',
            'cover_img',
            'original_price',
            'discount_price',
        ]


class ProductListSerializer(serializers.ModelSerializer):
    sku_set = SkuListSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'desc',
            'sku_set',
        ]
