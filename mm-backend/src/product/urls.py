from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    RecommendsAPIView,
    LoadMoreAPIView,
    CellphoneAPIView,
    )

urlpatterns = [
    path('recommends/', cache_page(1 * 10)(RecommendsAPIView.as_view()), name='recommends'),
    path('loadmore/', LoadMoreAPIView.as_view(), name='loadmore'),
    path('cellphone/', CellphoneAPIView.as_view(), name='cellphone'),
    # 以下分类标签数据接口和手机几乎一样，暂时不用做
    path('Intelligence//', RecommendsAPIView.as_view(), name='Intelligence'),
    path('tv/', RecommendsAPIView.as_view(), name='tv'),
    path('laptop//', RecommendsAPIView.as_view(), name='laptop'),
    path('appliance/', RecommendsAPIView.as_view(), name='appliance'),
    path('life/', RecommendsAPIView.as_view(), name='life'),
]
