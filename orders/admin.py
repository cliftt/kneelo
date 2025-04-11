from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'created_at')
    search_fields = ('name', 'phone', 'email')

