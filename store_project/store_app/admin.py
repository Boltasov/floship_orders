from django.contrib import admin

from .models import StoreOrder


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    readonly_fields = ["order_number", "status"]
