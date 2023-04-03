from django.contrib import admin
from django.urls import path, include
from shopapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories',views.CategoryViewset, basename="category" )
router.register(r'products',views.ProductViewset, basename="product" )
router.register(r'comments',views.CommentViewset, basename="comment" )
router.register(r'images',views.ImageViewset, basename="image")
router.register(r'orderrings',views.OrderringViewset, basename="orderring" )
router.register(r'billorders',views.BillOrderViewset, basename="billorder" )
router.register(r'policies', views.UserPolicyViewset, basename="policy")
# router.register(r'profile', views.ProfileViewset, basename="profile")

urlpatterns = router.urls + [
    path('profile/',views.Profile.as_view()),
]