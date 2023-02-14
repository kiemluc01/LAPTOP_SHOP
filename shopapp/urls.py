from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'departments',views.DepartmentViewset, basename="department" )

urlpatterns = router.urls + [
    # path('/', view),
]