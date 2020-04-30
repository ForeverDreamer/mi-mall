from django.contrib import admin

from .models import FileItem


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'upload_file', 'kb_size', 'active', 'created_time', 'update_time')
    # list_display_links = ('owner',)
    list_editable = ('title', 'active',)
    readonly_fields = ('size',)

    class Meta:
        model = FileItem


admin.site.register(FileItem, FileAdmin)
