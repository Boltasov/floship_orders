import requests
import posixpath
from os import environ
from dotenv import load_dotenv

from django.db.models.signals import post_save
from django.dispatch import receiver

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
