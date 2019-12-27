from rest_framework.exceptions import APIException
from mm.exceptions import MmException


class InventoryShortage(MmException, APIException):
    status_code = 503
    default_detail = '库存不足.'
    default_code = '696969'
