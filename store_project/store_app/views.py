from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import StoreOrder
from .serializers import StoreOrderSerializer


class StoreOrderView(ModelViewSet):
    queryset = StoreOrder.objects.all()
    serializer_class = StoreOrderSerializer

