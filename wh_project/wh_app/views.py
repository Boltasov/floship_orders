from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from wh_app.models import WarehouseOrder
from wh_app.serializers import WarehouseOrderSerializer


class WarehouseOrderView(ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
    permission_classes = (IsAuthenticated, )
