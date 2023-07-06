from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import WarehouseOrder, StoreAccount
from .serializers import WarehouseOrderSerializer, StoreAccountSerializer


class WarehouseOrderView(ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
    permission_classes = (IsAuthenticated, )


class StoreAccountView(ModelViewSet):
    queryset = StoreAccount.objects.all()
    serializer_class = StoreAccountSerializer
    permission_classes = (IsAuthenticated, )
