from django.contrib import admin
from django.urls import include, path
from usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Feed, name='feed'),
    path('auth/', include('usuarios.urls')),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)