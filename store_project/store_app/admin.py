from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import StoreOrder, WarehouseAccount
from .wh_api import wh_api


@admin.register(StoreOrder)
class StoreOrderAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['order_number', 'status', 'warehouse_account']
        else:
            return []


@admin.register(WarehouseAccount)
class WarehouseAccountAdmin(admin.ModelAdmin):
    readonly_fields = ['token']

    wh_base_url = 'http://127.0.0.1:8002'
    users_path = 'api/auth/users/'
    get_token_path = 'auth/token/login'
    accounts_path = 'api/stores/'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Регистрация нового пользователя
            name = obj.name
            password = User.objects.make_random_password()

            wh_api.create_user(name=name,
                               password=password,
                               wh_url=self.wh_base_url,
                               users_path=self.users_path)

            # Получение токена
            token = wh_api.get_token(name=name,
                                     password=password,
                                     wh_url=self.wh_base_url,
                                     get_token_path=self.get_token_path)

            obj.token = f'Token {token}'

            # Добавление магазина в склад, если ещё ни одного нет
            store_token, token_created = Token.objects.get_or_create(user=request.user)

            if token_created:
                wh_api.create_store_account(wh_url=self.wh_base_url,
                                            accounts_path=self.accounts_path,
                                            token=token,
                                            store_token=store_token)
        
        super().save_model(request, obj, form, change)


