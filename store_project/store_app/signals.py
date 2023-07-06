from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

import requests
from os import environ
import posixpath
from dotenv import load_dotenv

from .models import StoreOrder
from .serializers import StoreOrderSerializer


@receiver(post_save, sender=StoreOrder)
def send_order(sender, instance, created, **kwargs):
    if created:
        load_dotenv()

        store_url = environ['WH_URL']
        api_address = 'api/orders/'
        wh_url = posixpath.join(store_url, api_address)

        order_serialized = StoreOrderSerializer(instance)

        response = requests.post(wh_url, data=order_serialized.data)
        response.raise_for_status()
