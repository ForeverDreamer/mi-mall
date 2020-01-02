import time


def calculate_transport_costs(products_price):
    if products_price > 99:
        tc = 0
    else:
        tc = 10
    return tc


def get_order_no():
    order_no = 'order_' + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) \
               + str(time.time()).replace('.', '')[-7:]
    return order_no


def get_refund_no():
    refund_no = 'refund_' + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) \
                + str(time.time()).replace('.', '')[-7:]
    return refund_no
