from rest_framework.exceptions import APIException


class InventoryShortage(APIException):
    status_code = 503
    default_detail = '库存不足.'
    default_code = '696969'
