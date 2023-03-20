from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from shopapp import base_models
# Create your models here.  

POLICY_STATUS = (
    (0, 'Admin'),
    (1, 'Staff'),
    (2, 'Custommer'),
)
class UserPolicy(base_models.BaseCreateUpdateModel):
    name = models.IntegerField("Policy Name", choices=POLICY_STATUS)
    description = models.CharField("Desription", max_length=200)
    
class Userprofile(base_models.BaseCreateUpdateModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_user')
    root_image = models.ImageField(upload_to="image_user/", null=True)
    policy = models.ForeignKey("shopapp.UserPolicy", default=1,related_name="policy", on_delete=models.CASCADE)
    SDT = models.CharField("SDT", max_length=50, unique=True)
    addr = models.CharField("Addr", max_length=254)
    
    def __str__(self):
        return "Userprofile<{}>: {}".format(self.pk, self.user.username)
class Wallet(base_models.BaseCreateUpdateModel):
    code = models.CharField("Code", max_length=50, unique=True)
    user = models.ForeignKey("shopapp.Userprofile", related_name="user_wallet", on_delete=models.CASCADE)
    balance = models.IntegerField("Balance",default=0)
    is_active = models.BooleanField("Active", default=True)
    wallet_history = HistoricalRecords()
    
    def __str__(self):
        return "CreditCard<{}>: {}".format(self.pk, self.code)
    
class ProductCategory(base_models.BaseCreateUpdateModel):
    name = models.CharField("Name", max_length=150, unique=True)
    code = models.CharField("Code", max_length=50, unique=True)
    category_history = HistoricalRecords()
    
    def __str__(self):
        return "ProductCategory<{}>: {}".format(self.pk, self.name)

class Product(base_models.BaseCreateUpdateModel):
    name = models.CharField("Name", max_length=150)
    rootImage = models.ImageField(upload_to="media/", null=True)
    price = models.IntegerField("Price", default=0)
    productcategory = models.ForeignKey("shopapp.ProductCategory", blank=True, related_name="product_category", on_delete=models.CASCADE)
    product_history = HistoricalRecords()
    
    def __str__(self):
        return "Product<{}>: {}".format(self.pk, self.name)
    
class Comment(base_models.BaseCreateUpdateModel):
    content = models.CharField("Content", null=True, max_length=1000)
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    product = models.ForeignKey("shopapp.Product", blank=True ,  on_delete=models.CASCADE)
    
class Image(base_models.BaseCreateUpdateModel):
    name = models.CharField("Name", max_length=100, null=False)
    image = models.ImageField(upload_to='image_product/', null=True)
    product = models.ForeignKey("shopapp.Product", blank=True ,  on_delete=models.CASCADE)
    
class Orderring(base_models.BaseCreateUpdateModel):
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    product = models.ForeignKey("shopapp.Product", blank=True ,  on_delete=models.CASCADE)
    quanlity = models.IntegerField("quanlity", default=1)
    
class BillOrder(base_models.BaseCreateUpdateModel):
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    product = models.ForeignKey("shopapp.Product", blank=True ,  on_delete=models.CASCADE)
    quanlity = models.IntegerField("quanlity", default=1)
    code = models.CharField("Code", max_length=50)
    bill_history = HistoricalRecords()