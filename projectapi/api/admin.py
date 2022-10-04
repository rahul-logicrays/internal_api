from django.contrib import admin
from .models import SalesHistory

# Register your models here.


@admin.register(SalesHistory)
class AdminSalesHistory(admin.ModelAdmin):
    list_display = ['saleshistory_id']
