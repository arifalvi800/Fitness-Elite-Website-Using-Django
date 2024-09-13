from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="fitness Elite"
admin.site.site_title="fitness Elite"
admin.site.index_title="Welcome to fitness Elite Portal"

urlpatterns = [
    path('',views.index,name='index'),
    path('message',views.message,name='message')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)