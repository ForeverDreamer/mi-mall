from rest_framework.exceptions import APIException
from rest_framework import status


class MmException:
    pass


class ParameterError(MmException, APIException):
    status_code = 400
    default_code = '696969'


class MyAuthenticationFailed(MmException, APIException):
    status_code = status.HTTP_401_UNAUTHORIZED


class MyNotAuthenticated(MmException, APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
