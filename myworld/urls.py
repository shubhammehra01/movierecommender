
from django.contrib import admin
from django.conf import settings
from django.urls import path,include,re_path
from django.conf.urls.static import static

from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')), 
]
