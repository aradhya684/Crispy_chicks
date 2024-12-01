from django.contrib import admin
from .models import Order
# Register your models here.


class userorder(admin.ModelAdmin):
    list_display = ['user','order_id','created_at']

admin.site.register(Order,userorder)