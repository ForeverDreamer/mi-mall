from rest_framework.exceptions import APIException
from rest_framework import status


class MmException:
    pass


class ParameterError(MmException, APIException):
    status_code = 400
    default_code = '696969'


# 这个问题升级djangorestframework版本应该就能修复，不需要这么做, 后续：升级到djangorestframework==3.11.0还是没有，暂时不管了
# 不知道是不是官方故意这样设计的：把401自动替换为403
class MyAuthenticationFailed(MmException, APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


class MyNotAuthenticated(MmException, APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
