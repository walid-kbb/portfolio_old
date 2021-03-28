from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from main import views

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^$', include('main.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns