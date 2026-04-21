from django.urls import path
from .views import collection_language

app_name = "collection"

urlpatterns = [
    # ========================= COLLECTION ============================
    path("", collection_language, name="collection_home"),
    path("<str:lang>/", collection_language, name="collection_language"),
    path("<str:lang>/<str:topic>/", collection_language, name="collection_topic"),
]
