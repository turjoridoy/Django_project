from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=250)


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    img = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    date = models.CharField(max_length=1000)


