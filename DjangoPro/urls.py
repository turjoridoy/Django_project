from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from scraper.views import print_list, index

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', include('news.urls')),
    url(r'^scraper/', index),
]
