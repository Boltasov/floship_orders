from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

import requests
from os import environ
import posixpath
from dotenv import load_dotenv

from .models import WarehouseOrder
from .serializers import WarehouseStatusSerializer


@receiver(post_save, sender=WarehouseOrder)
def send_order(sender, instance, created, **kwargs):
    if not created:
        load_dotenv()

        store_url = environ['STORE_URL']
        api_path = 'api/orders/'
        order_url = posixpath.join(store_url, api_path, f'{str(instance.id)}/')

        headers = {
            'Authorization': 'Token da41cba48c949848464dd3f050cecfef4eb32bbb'
        }

        order_serialized = WarehouseStatusSerializer(instance)

        response = requests.patch(order_url, headers=headers, data=order_serialized.data)
        response.raise_for_status()
