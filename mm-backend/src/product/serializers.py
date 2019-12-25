from rest_framework import serializers

from .models import FirstCategory, AdProduct, Product


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


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'desc',
            'cover_img',
            'original_price',
            'discount_price',
        ]
