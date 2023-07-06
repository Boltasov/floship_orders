from django.contrib import admin

from store_app.models import StoreOrder


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    pass
