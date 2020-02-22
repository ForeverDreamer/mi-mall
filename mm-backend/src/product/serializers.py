from rest_framework import serializers

from .models import FirstCategory, AdProduct, Product, ProductCarouselImage, Sku


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


class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = [
            'id',
            'version',
            'color',
            'cover_img',
            'original_price',
            'discount_price',
        ]


class ProductCarouselImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCarouselImage
        fields = [
            'image'
        ]


class ProductSerializer(serializers.ModelSerializer):
    sku_set = SkuSerializer(many=True, read_only=True)
    carouse_images = ProductCarouselImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'desc',
            'carouse_images',
            'sku_set',
        ]
