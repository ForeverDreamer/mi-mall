from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.core import serializers
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


from .models import FirstCategory, SecondCategory, ThemeActivity, AdProduct, Product, Sku

admin.site.register(FirstCategory)
admin.site.register(SecondCategory)
admin.site.register(ThemeActivity)
admin.site.register(AdProduct)


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response


def export_selected_objects(modeladmin, request, queryset):
    selected = queryset.values_list('pk', flat=True)
    ct = ContentType.objects.get_for_model(queryset.model)
    return HttpResponseRedirect('/export/?ct=%s&ids=%s' % (
        ct.pk,
        ','.join(str(pk) for pk in selected),
    ))


export_as_json.short_description = "导出数据到json"
export_selected_objects.short_description = "导出数据到网页"

admin.site.add_action(export_as_json, 'export_json')
admin.site.add_action(export_selected_objects, 'export_view')


class SkuInline(admin.TabularInline):
    model = Sku


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'first_category', 'second_category', 'theme_activity', 'is_active']
    ordering = ['title']
    actions = ['bulk_online', 'bulk_offline']
    inlines = [SkuInline]

    def bulk_online(self, request, queryset):
        rows_updated = queryset.update(is_active=True)
        self.message_user(request, '上线了{}个商品'.format(rows_updated))

    bulk_online.short_description = "商品批量上线"

    def bulk_offline(self, request, queryset):
        rows_updated = queryset.update(is_active=False)
        self.message_user(request, '下线了{}个商品'.format(rows_updated))

    bulk_offline.short_description = "商品批量下线"

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
