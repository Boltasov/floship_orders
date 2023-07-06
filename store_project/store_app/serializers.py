from rest_framework.serializers import ModelSerializer, UUIDField

from store_app.models import StoreOrder


class StoreOrderSerializer(ModelSerializer):

    class Meta:
        model = StoreOrder
        fields = '__all__'
