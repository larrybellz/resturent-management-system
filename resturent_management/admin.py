from django.contrib import admin
from .models import StockItem ,Category,Stock


# Register your models here.

admin.site.register(StockItem)
admin.site.register(Category)
admin.site.register(Stock)