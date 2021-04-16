from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from src.account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    # can;t change this fields manually
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ('email', )
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
