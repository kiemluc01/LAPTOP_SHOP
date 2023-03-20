from django.urls import path, include
from chatbox import views

urlpatterns =  [
    # path('/', view),
    path('chatbox/',views.ChatAI.as_view()),
]