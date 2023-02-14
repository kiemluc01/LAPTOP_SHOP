from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(name=("Name"), max_length=150, unique=True)
    code = models.CharField(name=("Code"), max_length=50)
    
    def __str__(self):
        return "Department<{}>: {}".format(self.pk, self.name)
    
class CreditCard(models.Model):
    code = models.CharField(name=("Code"), max_length=50, unique=True)
    department = models.ForeignKey(Department, null=True, blank=True,  on_delete=models.CASCADE)
    balance = models.IntegerField(name=("Balance"),default=0)
    is_active = models.BooleanField(name=("Active"), default=True)
    
    def __str__(self):
        return "CreditCard<{}>: {}".format(self.pk, self.code)

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    SDT = models.CharField(name="SDT", max_length=50, unique=True)
    credit_card =models.ForeignKey("CreditCard", null=True, blank=True,  on_delete=models.CASCADE)
    addr = models.CharField(name="Addr", max_length=254)
    
    def __str__(self):
        return "Userprofile<{}>: {}".format(self.pk, self.user.username)
    
class ProductCategory(models.Model):
    name = models.CharField(name=("Name"), max_length=150, unique=True)
    code = models.CharField(("Code"), max_length=50, unique=True)
    
    def __str__(self):
        return "ProductCategory<{}>: {}".format(self.pk, self.name)

class Product(models.Model):
    name = models.CharField(name=("Name"), max_length=150)
    rootImage = models.CharField("RootImage", max_length=254, default=None)
    price = models.IntegerField(name=("Price"), default=0)
    productcategory = models.ForeignKey(ProductCategory, null=True, blank=True,  on_delete=models.CASCADE)
    quanlity_remaining = models.IntegerField(name=("Quanlity_remaining"), default=0)
    
    def __str__(self):
        return "Product<{}>: {}".format(self.pk, self.name)
    
class Comment(models.Model):
    content = models.CharField(name=("Content"), max_length=1000)
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    product = models.ForeignKey("Product", null=True, blank=True ,  on_delete=models.CASCADE)
    
class Image(models.Model):
    name = models.CharField(name=("Name"), max_length=100, null=False)
    src = models.CharField(name=("Src"), max_length=254, null=False)
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    product = models.ForeignKey("Product", null=True, blank=True ,  on_delete=models.CASCADE)
    
class Orderring(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True ,  on_delete=models.CASCADE)
    quanlity = models.IntegerField(name=("quanlity"), default=1)
    
class BillOrder(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True ,  on_delete=models.CASCADE)
    quanlity = models.IntegerField(name=("quanlity"), default=1)
    code = models.CharField(name=("Code"), max_length=50, null=False)