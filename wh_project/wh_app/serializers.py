from rest_framework.serializers import ModelSerializer, UUIDField

from .models import WarehouseOrder


class WarehouseOrderSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = WarehouseOrder
        fields = '__all__'


class WarehouseStatusSerializer(ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = ['status']
