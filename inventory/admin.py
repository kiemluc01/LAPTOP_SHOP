from django.contrib import admin
from inventory.models import Province, District, Ward, Inventory, InventoryItem,InventoryItemSerial, CPU,Ram, InventoryIn, \
InventoryInItem
# Register your models here.

admin.site.register(Province)
admin.site.register(District)
admin.site.register(Ward)
admin.site.register(Inventory)
admin.site.register(InventoryItem)
admin.site.register(InventoryIn)
admin.site.register(InventoryInItem)
admin.site.register(InventoryItemSerial)
admin.site.register(CPU)
admin.site.register(Ram)