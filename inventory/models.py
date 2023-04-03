from django.db import models
from simple_history.models import HistoricalRecords
# from django.contrib.gis.db import models as gis_models
# Create your models here.

class Province(models.Model):
    name = models.CharField("Provience Name", max_length=100)
    
    def __str__(self) -> str:
        return 'Province<{}>: {}'.format(self.country.name, self.name)
    
class District(models.Model):
    province = models.ForeignKey("inventory.Province", related_name="province", on_delete=models.CASCADE)
    name = models.CharField("District Name", max_length=100)
    
    def __str__(self) -> str:
        return 'District<{}>: {}'.format(self.province.name, self.name)
    
class Ward(models.Model):
    district = models.ForeignKey("inventory.District", related_name="district", on_delete=models.CASCADE)
    name = models.CharField("Ward Name", max_length=100)
    
    def __str__(self) -> str:
        return 'Ward<{}>: {}'.format(self.district.name, self.name)
    
class Inventory(models.Model):
    name = models.CharField("Name", max_length=150)
    ward = models.ForeignKey("inventory.Ward", related_name="ward", on_delete=models.CASCADE)
    addr_detail = models.CharField("Address Detail", max_length=250)
    # location = gis_models.PointField('Location', default='POINT(0 0)', srid=4326)
    
    def __str__(self) -> str:
        return 'Inventory<{}>: {}'.format(self.pk, self.name)
    
class InventoryItem(models.Model):
    item = models.ForeignKey("shopapp.Product", related_name="inventory_item_product", on_delete=models.CASCADE)
    inventory = models.ForeignKey("inventory.Inventory", related_name="inventory_item", on_delete=models.CASCADE)
    quantity = models.IntegerField("Amount", default=0)
    
INVENTORYIN_STATE = (
    (0, "step"),
    (1, "confirmed"),
)
class InventoryIn(models.Model):
    inventory = models.ForeignKey("inventory.Inventory", related_name="inventoryIn", on_delete=models.CASCADE)
    state = models.IntegerField("State", choices=INVENTORYIN_STATE)
    in_day = models.DateField("day input", auto_now_add=True)
    confirmed_at = models.DateField("confirmed At",null=True, blank=True)
    history = HistoricalRecords()
    
class InventoryInItem(models.Model):
    inventory_in = models.ForeignKey("inventory.InventoryIn", related_name="inventory_in_item", on_delete=models.CASCADE)
    name = models.CharField("Name Item", max_length=150)
    quantity = models.IntegerField("Amount", default=0)

INVENTORYOUT_STATE = (
    (0, "step"),
    (1, "confirmed"),
)
class InventoryOut(models.Model):
    inventory = models.ForeignKey("inventory.Inventory", related_name="inventoryOut", on_delete=models.CASCADE)
    state = models.IntegerField("State", choices=INVENTORYOUT_STATE)
    out_day = models.DateField("day output", auto_now_add=True)
    confirmed_at = models.DateField("confirmed At",null=True, blank=True)
    
class InventoryOutItem(models.Model):
    inventory_in = models.ForeignKey("inventory.InventoryOut", related_name="inventory_out_item", on_delete=models.CASCADE)
    name = models.CharField("Name Item", max_length=150)
    quantity = models.IntegerField("Amount", default=0)
    history = HistoricalRecords()