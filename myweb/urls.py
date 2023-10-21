from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from myweb.settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('staffpages/', include('staffpages.urls')),
] + static(settings.MEDIA_URL, document_root = MEDIA_ROOT)
