from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from DjangoPro import views
from news.models import Article
from news.views import *

urlpatterns = [
    url(r'^$/', views.index, name='index'),
]
