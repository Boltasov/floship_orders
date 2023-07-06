from django.contrib import admin

from .models import WarehouseOrder, StoreAccount


@admin.register(WarehouseOrder)
class WarehouseAdmin(admin.ModelAdmin):
    readonly_fields = ["order_number", "store_account"]

    def has_add_permission(self, request):
        return False


@admin.register(StoreAccount)
class StoreAccountAdmin(admin.ModelAdmin):
    pass
