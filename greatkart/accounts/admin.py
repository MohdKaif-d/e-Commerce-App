from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class Accountadmin(UserAdmin):
    list_display=('email','first_name','last_name','last_login','is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined') 
    orderning = ('date_joined',)
    filter_horizonatl = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account,Accountadmin)