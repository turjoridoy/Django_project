from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from news.models import Article
from news.views import *

router = SimpleRouter()

router.register('category', CategoryViewSet, 'UserViewSet')
router.register('article', ArticleViewSet, 'TeamViewSet')


urlpatterns = [
    # url('', include(router.urls), name='router'),
    url(r'^api/', include(router.urls), name='api'),
    url(r'^article/', article_by_category, name='old'),

]
