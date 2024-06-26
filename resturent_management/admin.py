from django.contrib import admin
from .models import StockItem ,Category,Stock,MenuItem


# Register your models here.

admin.site.register(StockItem)
admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(MenuItem)
