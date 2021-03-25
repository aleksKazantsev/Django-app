from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'blog/index.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat.slug,
    }

    return render(request, 'blog/post.html', context=context)

def show_category(request, cat_slug):
    posts = Post.objects.filter(cat__slug=cat_slug)

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected': cat_slug,
    }

    return render(request, 'blog/index.html', context=context)