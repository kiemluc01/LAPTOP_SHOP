from django.contrib import admin
from .models import UserPolicy,Userprofile, ProductCategory, Product, Comment, Image, Cart, CartItem, Bill, BillItem

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(UserPolicy)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Bill)
admin.site.register(BillItem)