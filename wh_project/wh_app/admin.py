from django.contrib import admin

from wh_app.models import WarehouseOrder


@admin.register(WarehouseOrder)
class WarehouseAdmin(admin.ModelAdmin):
    readonly_fields = ["order_number"]

    def has_add_permission(self, request):
        return False
