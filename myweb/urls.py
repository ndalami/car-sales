from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from myweb.settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),
] + static(settings.MEDIA_URL, document_root = MEDIA_ROOT)
