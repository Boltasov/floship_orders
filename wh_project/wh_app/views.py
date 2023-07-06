from rest_framework.viewsets import ModelViewSet

from .models import WarehouseOrder
from .serializers import WarehouseOrderSerializer


class WarehouseOrderView(ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
