from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.core import serializers
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect


from .models import FirstCategory, SecondCategory, ThemeActivity, AdProduct, Product, ProductCarouselImage, Sku
from .forms import SecondCategoryForm, SkuForm


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


class FirstCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'active', 'create_time', 'update_time')
    list_display_links = ('title',)
    # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
    list_editable = ('active', 'slug')

    class Meta:
        model = FirstCategory


admin.site.register(FirstCategory, FirstCategoryAdmin)


class SecondCategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_time'
    empty_value_display = '<空>'
    form = SecondCategoryForm
    fields = (
        'title', 'first_category', ('cover_img', 'img_height', 'img_width', 'link_url'), 'order', 'active',
        'create_time', 'update_time')
    list_display = ('title', 'first_category', 'order', 'active', 'create_time', 'update_time')
    list_display_links = ('title',)
    # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
    list_editable = ('first_category', 'order', 'active')
    list_filter = ('active', 'first_category', 'create_time', 'update_time')
    list_per_page = 10
    list_select_related = ('first_category',)
    ordering = ('title',)
    # radio_fields = {"first_category": admin.VERTICAL}
    search_fields = ['title', 'first_category__title']
    readonly_fields = ('img_height', 'img_width', 'create_time', 'update_time')

    class Meta:
        model = SecondCategory


admin.site.register(SecondCategory, SecondCategoryAdmin)


class AdProductAdmin(admin.ModelAdmin):
    list_display = ('location', 'link_url', 'image', 'image_width', 'image_height')
    list_display_links = ('location',)
    # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
    list_editable = ('link_url', 'image')

    class Meta:
        model = AdProduct


admin.site.register(AdProduct, AdProductAdmin)


class ThemeActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'link_url', 'cover_img', 'img_width', 'img_height', 'order', 'active',
                    'create_time', 'update_time')
    list_display_links = ('title',)
    # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
    list_editable = ('slug', 'link_url', 'cover_img', 'order', 'active')

    class Meta:
        model = ThemeActivity


admin.site.register(ThemeActivity, ThemeActivityAdmin)


class CarouselImageInline(admin.TabularInline):
    model = ProductCarouselImage
    # 只有一个foreign key可以不指定，有多个外键就必须要指定
    fk_name = "product"
    fields = ('id', 'image', 'image_width', 'image_height')
    readonly_fields = ('id', 'image_width', 'image_height')
    extra = 1


class SkuInline(admin.TabularInline):
    model = Sku
    # 只有一个foreign key可以不指定，有多个外键就必须要指定
    fk_name = "product"
    form = SkuForm
    fields = ('id', 'version', 'color', 'cover_img', 'img_width', 'img_height', 'original_price', 'discount_price',
              'min_purchase_num', 'max_purchase_num', 'inventory', 'is_active',)
    readonly_fields = ('id', 'img_height', 'img_width')
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_desc', 'first_category', 'second_category', 'theme_activity', 'is_active',
                    'create_time', 'update_time')
    list_display_links = ('title',)
    # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
    list_editable = ('first_category', 'second_category', 'theme_activity', 'is_active')
    ordering = ['title']
    actions = ['bulk_online', 'bulk_offline']
    inlines = [CarouselImageInline, SkuInline]
    date_hierarchy = 'create_time'
    empty_value_display = '<空>'
    # list_select_related = True
    autocomplete_fields = ['second_category']
    raw_id_fields = ("theme_activity",)

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
