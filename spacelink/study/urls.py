from django.urls import path
from .views import study_language

app_name = "study"

urlpatterns = [
    # =====================================================
    # LEVEL 1 & 2 — MAIN STUDY DASHBOARD
    # =====================================================
    # /study/
    path("", study_language, name="study-home"),

    # /study/python/
    # /study/java/
    path("<str:lang>/", study_language, name="study-language"),

    # /study/python/python-dsa/
    # /study/java/java-oops/
    path("<str:lang>/<str:topic>/", study_language, name="study-topic"),

]

