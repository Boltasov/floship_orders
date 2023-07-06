from rest_framework.serializers import ModelSerializer, UUIDField

from .models import WarehouseOrder, StoreAccount


class WarehouseOrderSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = WarehouseOrder
        fields = ['id', 'order_number', 'status']


class WarehouseStatusSerializer(ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = ['status']


class StoreAccountSerializer(ModelSerializer):
    class Meta:
        model = StoreAccount
        fields = ['name', 'token']
