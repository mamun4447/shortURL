from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from django.conf import settings

from app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

    urls(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    urls(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
