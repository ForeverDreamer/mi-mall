from rest_framework.exceptions import APIException


class MmException:
    pass


class ParameterError(MmException, APIException):
    status_code = 400
    default_code = '696969'
