from django.contrib import admin

from .models import FirstCategory, SecondCategory, ThemeActivity, AdProduct, Product

admin.site.register(FirstCategory)
admin.site.register(SecondCategory)
admin.site.register(ThemeActivity)
admin.site.register(AdProduct)
admin.site.register(Product)
