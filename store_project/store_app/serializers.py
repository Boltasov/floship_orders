from rest_framework.serializers import ModelSerializer

from .models import StoreOrder


class StoreOrderSerializer(ModelSerializer):

    class Meta:
        model = StoreOrder
        fields = '__all__'
