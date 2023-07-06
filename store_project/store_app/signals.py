from os import environ
from dotenv import load_dotenv

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StoreOrder
from .serializers import StoreOrderSerializer
from .wh_api.wh_api import create_order


@receiver(post_save, sender=StoreOrder)
def send_order(sender, instance, created, **kwargs):
    if created:
        load_dotenv()
        wh_url = environ['WH_URL']
        orders_path = 'api/orders/'
        token = instance.warehouse_account.token

        order_serialized = StoreOrderSerializer(instance)

        create_order(order_serialized, wh_url, orders_path, token)
