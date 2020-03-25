from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


def index(request):
    all_cat = Category.objects.all()
    html = ''
    for cat in all_cat:
        url = '/news/' +str(cat.id)+ '/'
        html += '<a href="'+url+'"> '+cat.cat_name+'</a></br>'
    return HttpResponse(html)


def detail(request, cat_id):
    return HttpResponse("<h1>Hello, " +str(cat_id)+" </h1>")
