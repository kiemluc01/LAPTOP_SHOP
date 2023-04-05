from django.contrib import admin
from inventory.models import Province, District, Ward, Inventory, InventoryItem,InventoryItemSerial, CPU,Ram, InventoryIn, \
InventoryOut, InventoryInItem, InventoryOutItem
# Register your models here.

admin.site.register(Province)
admin.site.register(District)
admin.site.register(Ward)
admin.site.register(Inventory)
admin.site.register(InventoryItem)
admin.site.register(InventoryIn)
admin.site.register(InventoryOut)
admin.site.register(InventoryInItem)
admin.site.register(InventoryOutItem)
admin.site.register(InventoryItemSerial)
admin.site.register(CPU)
admin.site.register(Ram)