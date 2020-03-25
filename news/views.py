from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import Category, Article
from news.serializer import CategorySerializer, ArticleSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view(['GET'])
def article_by_category(request):
    if request.method == 'GET':
        category_from_brower = request.GET.get("categorys")
        articles = Article.objects.filter(category_id=category_from_brower)
        return Response(data=ArticleSerializer(articles, many=True).data,
                        status=status.HTTP_200_OK)
