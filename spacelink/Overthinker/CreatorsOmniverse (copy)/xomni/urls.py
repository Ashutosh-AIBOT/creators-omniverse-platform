from django.urls import path
from . import views

app_name = "xomni"

urlpatterns = [
    path("", views.chatbot_page, name="xomni"),
]
