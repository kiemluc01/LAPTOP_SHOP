from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/shopapp/', include('shopapp.urls')),
    path('api/v1/chatboxs/', include('chatbox.urls'))
]
