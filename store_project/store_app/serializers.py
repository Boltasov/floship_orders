from rest_framework.serializers import ModelSerializer, UUIDField

from .models import StoreOrder


class StoreOrderSerializer(ModelSerializer):
    id = UUIDField()

    class Meta:
        model = StoreOrder
        fields = ['id', 'order_number', 'status']
