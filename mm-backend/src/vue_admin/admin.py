from django.contrib import admin

from .models import AdminInfo, Menu, Submenu


# class AdminInfoInline(admin.TabularInline):
#     model = AdminInfo
#     fk_name = 'navMenu'
#     fields = ('id', 'name', 'avatar', 'width', 'height', 'active')
#     readonly_fields = ('id', 'width', 'height')
#     extra = 1


class AdminInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'active_index', 'avatar', 'active')
    list_display_links = ('owner',)
    # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
    list_editable = ('avatar', 'active_index', 'active')
    readonly_fields = ('width', 'height',)
    ordering = ['id']
    date_hierarchy = 'create_time'
    empty_value_display = '<空>'

    class Meta:
        model = AdminInfo


admin.site.register(AdminInfo, AdminInfoAdmin)


class SubmenuInline(admin.TabularInline):
    model = Submenu
    fk_name = 'menu'
    fields = ('id', 'menu', 'user_set', 'name', 'icon', 'url', 'active')
    readonly_fields = ('id',)
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'sub_active_index', 'active')
    # list_display_links = ('name',)
    # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
    list_editable = ('name', 'url', 'active')
    ordering = ['id']
    inlines = (SubmenuInline,)
    date_hierarchy = 'create_time'
    empty_value_display = '<空>'

    class Meta:
        model = Menu


admin.site.register(Menu, MenuAdmin)


# class MenuInline(admin.TabularInline):
#     model = Menu
#     fk_name = 'navMenu'
#     fields = ('id', 'name', 'url', 'sub_active_index', 'active')
#     readonly_fields = ('id',)
#     extra = 1
#     # inlines = (SubmenuInline,)

#
# class NavMenuAdmin(admin.ModelAdmin):
#     list_display = ('id', 'owner', 'active_index', 'active')
#     list_display_links = ('owner',)
#     # 修改时需要验证的字段例如'title'，不要放在list_editable中，这样会绕过ModelForm的验证机制
#     list_editable = ('active_index', 'active')
#     ordering = ['owner']
#     # inlines = (AdminInfoInline, MenuInline)
#     inlines = (MenuInline,)
#     date_hierarchy = 'create_time'
#     empty_value_display = '<空>'
#
#     class Meta:
#         model = NavMenu
#
#
# admin.site.register(NavMenu, NavMenuAdmin)
