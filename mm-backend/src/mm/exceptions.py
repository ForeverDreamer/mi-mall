from rest_framework.exceptions import APIException
from rest_framework import status


class MmException:
    pass


class ParameterError(MmException, APIException):
    status_code = 400
    default_code = '696969'


# 这个问题升级django版本应该就能修复，不需要这么做
class MyAuthenticationFailed(MmException, APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


class MyNotAuthenticated(MmException, APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
