from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', post_list, name="post_list_url"),
    path('post/<str:slug>/', post_detail, name="post_detail_url"),
    path('summernote/', include('django_summernote.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)