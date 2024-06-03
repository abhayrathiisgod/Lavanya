from django.contrib import admin
from .models import Category, Supplier, Product, InventoryTransaction, PurchaseOrder, PurchaseOrderItem, SalesOrder, SalesOrderItem
# Register your models here.


admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(InventoryTransaction)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)