from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from store_app.models import StoreOrder
from store_app.serializers import StoreOrderSerializer


class StoreOrderView(ModelViewSet):
    queryset = StoreOrder.objects.all()
    serializer_class = StoreOrderSerializer
    permission_classes = (IsAuthenticated, )

