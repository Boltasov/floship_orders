from django.contrib import admin

from .models import StoreOrder


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['order_number', 'status']
        else:
            return []

