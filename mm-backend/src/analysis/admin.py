from django.contrib import admin


from .models import Config, SendCodeLog, UserLoginLog


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'send_code_times_limit', 'login_times_limit')
    list_display_links = ('id',)
    list_editable = ('send_code_times_limit', 'login_times_limit')

    class Meta:
        model = Config


admin.site.register(Config, ConfigAdmin)


class SendCodeLogAdmin(admin.ModelAdmin):
    list_display = ('phone', 'veri_code', 'create_time')
    list_display_links = None
    readonly_fields = ('phone', 'veri_code')

    class Meta:
        model = SendCodeLog


admin.site.register(SendCodeLog, SendCodeLogAdmin)


class UserLoginLogAdmin(admin.ModelAdmin):
    list_display = ('owner', 'login_type', 'login_name', 'create_time')
    list_display_links = None
    readonly_fields = ('owner', 'login_type', 'login_name')

    class Meta:
        model = UserLoginLog


admin.site.register(UserLoginLog, UserLoginLogAdmin)
