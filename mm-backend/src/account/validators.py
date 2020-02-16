import re


def is_phone(phone):
    pattern = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
    result = re.search(pattern, phone)
    if result is None:
        return False
    else:
        return True


def is_veri_code(veri_code):
    return True
