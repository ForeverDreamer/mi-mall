from rest_framework import serializers

from .models import AdminInfo, Menu, Submenu


class AdminInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInfo
        fields = [
            'name',
            'active_index',
            'avatar'
        ]


class SubmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submenu
        fields = [
            'name',
            'icon',
            'url'
        ]


class MenuSerializer(serializers.ModelSerializer):
    # submenus = SubmenuSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = [
            'name',
            'url',
            'sub_active_index',
            # 'submenus'
        ]


class ResMenuSerializer(serializers.ModelSerializer):
    submenus = SubmenuSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = [
            'name',
            'url',
            'sub_active_index',
            'submenus'
        ]


# class NavMenuSerializer(serializers.ModelSerializer):
#     menus = MenuSerializer(many=True, read_only=True)
#     admininfo = AdminInfoSerializer(read_only=True)
#
#     class Meta:
#         model = NavMenu
#         fields = [
#             'active_index',
#             'menus',
#             'admininfo',
#         ]


class NavSerializer(serializers.Serializer):
    # menus = MenuSerializer(many=True, read_only=True)
    admin_info = AdminInfoSerializer(read_only=True)
