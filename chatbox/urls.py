from django.urls import path, include
from chatbox import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'history_chats', views.ChatAIViewset, basename='history_chat')

urlpatterns = router.urls + [
    # path('/', view),
    path('chatbox/',views.ChatAI.as_view()),
]