from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory import views

router = DefaultRouter()
router.register(r'provinces', views.ProvinceViewset, basename='province')
router.register(r'districts', views.DistrictViewset, basename='district')
router.register(r'wards', views.WardViewset, basename='ward')

urlpatterns = router.urls + [
    
]
