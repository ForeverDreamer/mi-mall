from django.utils import timezone

from rest_framework_simplejwt.tokens import RefreshToken

from analysis.models import Config, UserLoginLog


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# 判断该用户当日登录次数是否超过警戒值，是则禁用该用户，返回错误信息，记录错误日志
def is_login_too_often(user):
    login_times_limit = Config.objects.first().login_times_limit
    today_times = UserLoginLog.objects.filter(create_time__date=timezone.now().date()).count()
    if today_times >= login_times_limit:
        user.is_active = False
        user.save()
        return True
    return False
