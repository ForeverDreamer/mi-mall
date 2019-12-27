from rest_framework import generics

from .models import ShippingAddress
from .serializers import (
    ShippingAddressListCreateSerializer,
    ShippingAddressUpdateSerializer,
)


class ShippingAddressListCreateView(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressListCreateSerializer


class ShippingAddressUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressUpdateSerializer
