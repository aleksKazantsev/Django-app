from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Все статьи')

def categories(request, catid):
    return HttpResponse(f"Статьи по категориям{catid}")