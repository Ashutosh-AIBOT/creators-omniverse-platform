from django.urls import path
from .views import home_view

app_name = "universe"

urlpatterns = [
    path("", home_view, name="phome"),                       # Before login page
    path("home/<str:username>/", home_view, name="home"),    # After login page with username in URL
]
