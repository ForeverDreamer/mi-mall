from django.utils import timezone

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from analysis.models import Config, UserLoginLog
from vue_admin.models import AdminInfo, Menu
from vue_admin.serializers import AdminInfoSerializer, MenuSerializer, SubmenuSerializer


def get_tokens_for_user(user):
    access_token = AccessToken.for_user(user)

    return {
        'exp': access_token['exp'],
        'access': access_token['jti'],
    }


# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


# 判断该用户当日登录次数是否超过警戒值，是则禁用该用户，返回错误信息，记录错误日志
def is_login_too_often(user):
    login_times_limit = Config.objects.first().login_times_limit
    today_times = UserLoginLog.objects.filter(create_time__date=timezone.now().date()).count()
    if today_times >= login_times_limit:
        user.is_active = False
        user.save()
        return True
    return False


def admin_login(user):
    if not user.is_staff:
        return
    menus = Menu.objects.all()
    # tmp_menus = menus.values()
    admin_info = AdminInfoSerializer(AdminInfo.objects.by_user(user).first()).data
    tmp_menus = []
    urls = []
    for menu in menus:
        if user in menu.user_set.all():
            tmp_submenus = []
            for submenu in menu.submenus.all():
                if user in submenu.user_set.all():
                    tmp_submenu = SubmenuSerializer(submenu).data
                    urls.append(tmp_submenu['url'])
                    tmp_submenus.append(tmp_submenu)
            tmp_menu = MenuSerializer(menu).data
            # urls.append(tmp_menu['url'])
            tmp_menu['submenus'] = tmp_submenus
            tmp_menus.append(tmp_menu)
    nav = {
        'menus': tmp_menus,
        'admin_info': admin_info,
        'permitted_routes': urls,
    }
    # for menu, nav_menu in zip(menus, nav['menus']):
    #     # menu.submenus = menu.submenus.by_user(user)
    #     submenus = menu.submenus.all()
    #     temp_submenus = []
    #     for submenu in submenus:
    #         if user in submenu.user_set.all():
    #             temp_submenus.append(SubmenuSerializer(submenu).data)
    #     nav_menu['submenus'] = temp_submenus
    # nav_menu = NavMenuSerializer(NavMenu.objects.first()).data
    # if not user.is_superuser:
    #     nav_menu = NavMenuSerializer(NavMenu.objects.first()).data
    return nav
