"""
URL configuration for tradecore project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    path("accounts/", include("accounts.urls")),
    path("kpi/", include("kpi.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# BULLETPROOF FIX: Force Django to explicitly serve static files in development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()