from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("7309913032/", admin.site.urls),
    
    # ROOT FRONTEND
    path("", include("universe.urls")),
    
    path("testaccounts/", include("testaccounts.urls")),
    path("testprofiles/", include("testprofiles.urls")),
    path("study/", include("study.urls")),
    path("collection/", include("collection.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("xomni/", include("xomni.urls")),
    path("communities/", include("communities.urls")),
]

    
if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)