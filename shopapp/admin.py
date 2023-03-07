from django.contrib import admin
from .models import UserPolicy,Userprofile, ProductCategory, Product, Comment, Image, Orderring, BillOrder

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(UserPolicy)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Orderring)
admin.site.register(BillOrder)
