from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'departments',views.DepartmentViewset, basename="department" )
router.register(r'profile',views.ProfileViewset, basename="profile" )
router.register(r'creditcards',views.CreditCardViewset, basename="creditcard" )
router.register(r'categories',views.CategoryViewset, basename="category" )
router.register(r'products',views.ProductViewset, basename="product" )
router.register(r'comments',views.CommentViewset, basename="comment" )
router.register(r'images',views.ImageViewset, basename="image" )
router.register(r'orderrings',views.OrderringViewset, basename="orderring" )
router.register(r'billorders',views.BillOrderViewset, basename="billorder" )

urlpatterns = router.urls + [
    # path('/', view),
]