from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import FirstCategory, SecondCategory, ThemeActivity, AdProduct, Product, Sku

admin.site.register(FirstCategory)
admin.site.register(SecondCategory)
admin.site.register(ThemeActivity)
admin.site.register(AdProduct)


class SkuInline(admin.TabularInline):
    model = Sku


class ProductAdmin(admin.ModelAdmin):
    inlines = [SkuInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
