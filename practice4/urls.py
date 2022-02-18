from django.contrib import admin
from django.urls import path as pa
from django.urls import include
from django.views.static import serve
from django.conf import settings

from app import urls

urlpatterns = [
    pa('admin/', admin.site.urls),
    pa('', include('app.urls')),

]
