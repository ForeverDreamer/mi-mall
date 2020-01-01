import os
from datetime import datetime as dt

from django.utils import timezone

from rest_framework.views import exception_handler

from mm.exceptions import MmException


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None and isinstance(exc, MmException):
        # response.data['status_code'] = response.status_code
        response.data['error_code'] = exc.get_codes()

    return response


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def before_datetime(t):
    if timezone.now() < t:
        return True
    return False


def after_datetime(t):
    if timezone.now() > t:
        return True
    return False
