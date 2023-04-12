from django.db import models
from simple_history.models import HistoricalRecords
from shopapp import base_models
import random
# from django.contrib.gis.db import models as gis_models
# Create your models here.

class Province(base_models.BaseCreateUpdateModel):
    name = models.CharField("Provience Name", max_length=100)
    
    def __str__(self) -> str:
        return 'Province<{}>: {}'.format(self.country.name, self.name)
    
class District(base_models.BaseCreateUpdateModel):
    province = models.ForeignKey("inventory.Province", related_name="province", on_delete=models.CASCADE)
    name = models.CharField("District Name", max_length=100)
    
    def __str__(self) -> str:
        return 'District<{}>: {}'.format(self.province.name, self.name)
    
class Ward(base_models.BaseCreateUpdateModel):
    district = models.ForeignKey("inventory.District", related_name="district", on_delete=models.CASCADE)
    name = models.CharField("Ward Name", max_length=100)
    
    def __str__(self) -> str:
        return 'Ward<{}>: {}'.format(self.district.name, self.name)
    
class Inventory(base_models.BaseCreateUpdateModel):
    name = models.CharField("Name", max_length=150)
    ward = models.ForeignKey("inventory.Ward", related_name="ward", on_delete=models.CASCADE)
    addr_detail = models.CharField("Address Detail", max_length=250)
    # location = gis_models.PointField('Location', default='POINT(0 0)', srid=4326)
    
    def __str__(self) -> str:
        return 'Inventory<{}>: {}'.format(self.pk, self.name)
    
    
class Ram(base_models.BaseCreateUpdateModel):
    name = models.CharField("name", max_length=100, unique=True, blank=True)
    price = models.IntegerField("Price", default=0)
    
class CPU(base_models.BaseCreateUpdateModel):
    name = models.CharField("name", max_length=100, unique=True, blank=True)
    price = models.IntegerField("Price", default=0)
class InventoryItem(base_models.BaseCreateUpdateModel):
    item = models.ForeignKey("shopapp.BaseProduct", related_name="inventory_item_product", on_delete=models.CASCADE)
    inventory = models.ForeignKey("inventory.Inventory", related_name="inventory_item", on_delete=models.CASCADE)
    quantity = models.IntegerField("Amount", default=0)
    ram = models.ForeignKey("inventory.Ram", related_name="product_ram", null=True, blank=True, on_delete=models.CASCADE)
    cpu = models.ForeignKey("inventory.CPU", related_name="product_cpu", null=True, blank=True, on_delete=models.CASCADE)
    
class InventoryItemSerial(base_models.BaseCreateUpdateModel):
    item = models.ForeignKey("inventory.InventoryItem", related_name="item_serial", on_delete=models.CASCADE)
    serial = models.CharField("Serial", max_length=50, default=random.randint(1000000000, 9999999999))
    
INVENTORYIN_STATE = (
    (0, "step"),
    (1, "confirmed"),
)
class InventoryIn(base_models.BaseCreateUpdateModel):
    inventory = models.ForeignKey("inventory.Inventory", related_name="inventoryIn", on_delete=models.CASCADE)
    state = models.IntegerField("State", choices=INVENTORYIN_STATE)
    in_day = models.DateField("day input", auto_now_add=True)
    confirmed_at = models.DateField("confirmed At",null=True, blank=True)
    history = HistoricalRecords()
class InventoryInItem(models.Model):
    inventory_in = models.ForeignKey("inventory.InventoryIn", related_name="inventory_in_item", on_delete=models.CASCADE)
    name = models.CharField("Name Item", max_length=150)
    quantity = models.IntegerField("Amount", default=0)