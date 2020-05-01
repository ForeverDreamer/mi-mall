"""mm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views
# from django.views.generic import TemplateView
# from django.views.generic import RedirectView
from django.contrib.staticfiles.views import serve

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )

from .views import home_view, export_view

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    # path('', RedirectView.as_view(permanent=True, url='static/index.html')),
    path('', home_view, name='home'),
    path('favicon.ico', serve, {'path': 'image/favicon.ico'}),
    path('admin/', admin.site.urls),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    # 不要直接暴露Token接口，要通过views对用户禁用，用户主动登出等情况加以验证
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('product/', include(('product.urls', 'product'), namespace='product')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('pay/', include(('pay.urls', 'pay'), namespace='pay')),
    # path('vue_admin/', include(('vue_admin.urls', 'vue_admin'), namespace='vue_admin')),
    path('export/', export_view, name='export'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
    path('license/', views.flatpage, {'url': '/license/'}, name='license'),
]
