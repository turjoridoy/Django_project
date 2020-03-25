from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.URLField(blank=True,
                            default='https://elysator.com/wp-content/uploads/blank-profile-picture-973460_1280-e1523978675847.png')
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'title'
    REQUIRED_FIELDS = []
