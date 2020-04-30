import re

from django.contrib import admin

from .models import FileItem


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file_path', 'kb_size', 'active', 'created_time', 'update_time')
    # list_display_links = ('owner',)
    list_editable = ('title', 'active',)
    readonly_fields = ('owner', 'size',)

    class Meta:
        model = FileItem

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        pattern = re.compile(r'^upload/')
        # 区分是上传文件自动修改，还是用户直接编辑title字段修改
        uploading = not re.search(pattern, obj.upload_file.name)
        if uploading:
            obj.title = obj.upload_file.name
            obj.size = obj.upload_file.size
        super().save_model(request, obj, form, change)


admin.site.register(FileItem, FileAdmin)
