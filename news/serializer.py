from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from news.models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
