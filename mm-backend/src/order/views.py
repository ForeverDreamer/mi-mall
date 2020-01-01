from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from mm.utils import before_datetime, after_datetime
from mm.exceptions import ParameterError
from .utils import calculate_transport_costs, get_order_no
from .models import ShippingAddress, Coupon, ORDER_STATUS, OrderItem, Order
from .serializers import (
    ShippingAddressListCreateSerializer,
    ShippingAddressUpdateSerializer,
    CouponListSerializer,
    ReceiveCouponCreateSerializer,
    ReceiveCouponListSerializer,
    OrderCreateSerializer,
    OrderListSerializer,
)

User = get_user_model()


class ShippingAddressListCreateAPIView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressListCreateSerializer


class ShippingAddressUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressUpdateSerializer


class CouponListAPIView(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponListSerializer


class CouponReceiveAPIView(generics.CreateAPIView):
    serializer_class = ReceiveCouponCreateSerializer

    def perform_create(self, serializer):
        owner = serializer.validated_data.get('owner')
        coupon = serializer.validated_data.get('coupon')
        coupon_list = owner.receivecoupon_set.all()
        for c in coupon_list:
            if coupon == c.coupon:
                raise ParameterError(detail="优惠券id:{}领取数量已达上限".format(coupon.id))
        serializer.save()


class CouponReceiveListAPIView(generics.ListAPIView):
    serializer_class = ReceiveCouponListSerializer

    def get_queryset(self):
        admin = User.objects.all().first()
        qs = admin.receivecoupon_set.all()
        return qs


class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer

    def perform_create(self, serializer):
        admin = User.objects.all().first()
        # 检测商品是否已加入购物车
        cart_items = self.request.data.get('cart_items')
        try:
            item_ids = [int(item_id) for item_id in cart_items.split(',')]
        except ValueError:
            raise ParameterError(detail="cart_items必须为整数")
        items = admin.cart.items.all()
        if not items.exists():
            raise ParameterError(detail="购物车是空的")
        item_dict = {item.id: item for item in items}
        sku_dict = {}
        item_list = []
        for item_id in item_ids:
            if item_id not in item_dict.keys():
                raise ParameterError(detail="商品 item_id={}不在购物车".format(item_id))
            # 库存是否足够
            if item_dict[item_id].sku.inventory < item_dict[item_id].purchase_num:
                raise ParameterError(detail="库存不足 sku_id={}".format(item_dict[item_id].sku.id))
            sku_dict[item_dict[item_id].sku.id] = item_dict[item_id].sku
            item_list.append(item_dict[item_id])
        coupon = serializer.validated_data.get('coupon')
        # 优惠券是否active，CouponManager只返回active的对象，serializer会提示优惠券不存在
        # if not coupon.active:
        #     raise ParameterError(detail="优惠券已下线")
        # 优惠券是否在使用时间范围内
        if before_datetime(coupon.start_time):
            raise ParameterError(detail="优惠券未到使用时间")
        if after_datetime(coupon.end_time):
            raise ParameterError(detail="优惠券已过期")
        # 用户是否领取该优惠券,且没有使用
        coupon_list = admin.receivecoupon_set.all()
        received = False
        coupon_received = None
        for c in coupon_list:
            if coupon == c.coupon:
                if c.used:
                    raise ParameterError(detail="该优惠券id:{}已经使用过".format(coupon.id))
                coupon_received = c
                received = True
        if not received:
            raise ParameterError(detail="用户没有领取过该优惠券id:{}".format(coupon.id))
        # 计算商品总价
        products_price = 0
        for sku in sku_dict.values():
            products_price += sku.discount_price
        # 抵扣优惠券
        products_price -= coupon.discount_amount
        # 计算运输费用
        transport_costs = calculate_transport_costs(products_price)
        # 等待客户端微信或支付宝完成支付，回调服务器接口，修改订单支付状态
        # success = True
        # if success:
        #     status = ORDER_STATUS[1][0]
        #
        # else:
        #     status = ORDER_STATUS[0][0]
        order_no = get_order_no()
        order = serializer.save(owner=admin, order_no=order_no, products_price=products_price,
                                transport_costs=transport_costs,
                                status=ORDER_STATUS[0][0])
        for item in item_list:
            sku = item.sku
            purchase_num = item.purchase_num
            sale_price = item.sku.discount_price
            order_item = OrderItem.objects.create(sku=sku, purchase_num=purchase_num, sale_price=sale_price)
            order.order_items.add(order_item)
        for item in item_list:
            # 扣减商品库存数量
            item.sku.inventory -= item.purchase_num
            item.sku.save()
            # 清除购物车中已结算的商品
            item.delete()

        # # 优惠券设置为已使用
        # coupon_received.used = True
        # coupon_received.save()
        # try:

        # except IntegrityError as e:
        #     raise ParameterError(detail='IntegrityError')


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=status']
    ordering_fields = ["-update_time"]
