from django.db import models
import uuid


class WarehouseAccount(models.Model):
    name = models.CharField(max_length=255, unique=True)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class StoreOrder(models.Model):
    STATUSES = [
        (1, 'New'),
        (2, 'In Progress'),
        (3, 'Stored'),
        (4, 'Send'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
        )
    order_number = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUSES, default=1)
    warehouse_account = models.ForeignKey(WarehouseAccount, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.order_number
