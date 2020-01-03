import logging

from django.conf import settings

from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import FirstCategory, AdProduct, ThemeActivity, Product, SecondCategory
from .serializers import ProductListSerializer

LOGGER_NAME = '{}.{}'.format(settings.PROJECT_NAME, __name__)
logger = logging.getLogger(LOGGER_NAME)


class RecommendsAPIView(APIView):
    def get(self, *args, **kwargs):
        first_category_list = FirstCategory.objects.values('title')
        ad_product_list = AdProduct.objects.values('location', 'image', 'link_url')
        theme_activity_list = ThemeActivity.objects.values('title', 'cover_img', 'link_url', 'order')
        product_list = Product.objects.values('title', 'desc')
        for p1, p2 in zip(product_list, Product.objects.all()):
            p1['sku_set'] = p2.sku_set.all().values('version', 'color', 'cover_img', 'original_price', 'discount_price')
        data = {
            'first_category_list': first_category_list,
            'ad_product_list': ad_product_list,
            'theme_activity_list': theme_activity_list,
            'product_list': product_list,
        }
        return Response({'data': data}, status=status.HTTP_200_OK)


class CellphoneAPIView(APIView):
    def get(self, *args, **kwargs):
        ad_product_list = AdProduct.objects.values('location', 'image', 'link_url')
        second_category_list = SecondCategory.objects.filter(first_category__slug='cellphone').values('title',
                                                                                                      'cover_img',
                                                                                                      'link_url',
                                                                                                      'order')
        product_list = Product.objects.values('title', 'desc')
        for p1, p2 in zip(product_list, Product.objects.all()):
            p1['sku_set'] = p2.sku_set.all().values('version', 'color', 'cover_img', 'original_price', 'discount_price')
        data = {
            'ad_product_list': ad_product_list,
            'second_category_list': second_category_list,
            'product_list': product_list,
        }
        return Response({'data': data}, status=status.HTTP_200_OK)


# 通过分页机制，客户端get传递limit和offset决定数据量
class LoadMoreAPIView(generics.ListAPIView):
    queryset = Product.objects.guess_you_like()
    serializer_class = ProductListSerializer
