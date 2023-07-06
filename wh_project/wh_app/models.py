from django.db import models
import uuid


class WarehouseOrder(models.Model):
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

    def __str__(self):
        return self.order_number
