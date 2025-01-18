from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from os import getenv

urlpatterns = [
    path(getenv('ADMIN_URL'), admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # Dil dəyişdirmək üçün URL
]

# Dil prefiksi ilə URL-ləri avtomaatik olaraq əlavə edir
urlpatterns += i18n_patterns(
    path('', include('info.urls')),
    path('', include('contact.urls')),
    path('', include('services.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
