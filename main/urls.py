from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', include(('mainapp.urls','mainapp'), namespace='mainapp')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Admin headers
admin.site.site_header = "Starwars"
admin.site.site_title = "Starwars Admin"
admin.site.index_title = "Welcome to Starwars Admin Panel"
