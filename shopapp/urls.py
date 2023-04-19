from django.contrib import admin
from django.urls import path, include
from shopapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',views.CategoryViewset, basename="category" )
router.register(r'products',views.ProductViewset, basename="product" )
router.register(r'comments',views.CommentViewset, basename="comment" )
router.register(r'images',views.ImageViewset, basename="image")
# router.register(r'orderrings',views.OrderringViewset.as_view(), basename="orderring" )
router.register(r'billorders',views.BillOrderViewset, basename="billorder" )
router.register(r'policies', views.UserPolicyViewset, basename="policy")
router.register(r'cart_items', views.CartItemViewset, basename="cart_items")
router.register(r'register', views.RegisterViewset, basename="register")

urlpatterns = router.urls + [
    path('profile/',views.Profile.as_view()),
    path('orderrings/',views.OrderringViewset.as_view()),
]