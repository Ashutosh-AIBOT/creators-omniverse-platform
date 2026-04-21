

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    
    # ROOT FRONTEND
    path("", include("universe.urls")),
    
    path("testaccounts/", include("testaccounts.urls")),
    path("testprofiles/", include("testprofiles.urls")),
    path("study/", include("study.urls")),
    path("collection/", include("collection.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("xomni/", include("xomni.urls")),
    
    ]

    

if  settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
