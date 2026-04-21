from django.urls import path
from . import views

app_name = "xomni"

urlpatterns = [
    path("", views.chatbot_page, name="xomni"),
    path("api/chat/", views.chat_api, name="chat_api"),
]
