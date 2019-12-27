from rest_framework import serializers

from .models import ShippingAddress


class ShippingAddressListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            'id',
            'owner',
            'name',
            'cell_phone',
            'province',
            'county',
            'town',
            'street',
            'tag',
            'is_default',
        ]
        extra_kwargs = {'id': {'read_only': True}, 'owner': {'write_only': True}}


class ShippingAddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = [
            'id',
            'name',
            'cell_phone',
            'province',
            'county',
            'town',
            'street',
            'tag',
            'is_default',
        ]
        extra_kwargs = {'id': {'read_only': True}}
