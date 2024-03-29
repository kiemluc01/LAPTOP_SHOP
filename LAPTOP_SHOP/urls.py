from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/shopapp/', include('shopapp.urls')),
    path('api/v1/chatboxs/', include('chatbox.urls')),
    path('api/v1/inventory/', include('inventory.urls')),
    
    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
