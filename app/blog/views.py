from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_post'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

class BlogHome(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)

#def index(request):
#    posts = Post.objects.all()
#
#    context = {
#        'posts': posts,
#        'menu': menu,
#        'title': 'Главная страница',
#        'cat_selected': 0,
#    }
#
#    return render(request, 'blog/index.html', context=context)

def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О сайте'})

class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление поста'
        return context


#def addpost(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#
#    else:
#        form = AddPostForm()
#    return render(request, 'blog/addpost.html', {'form': form, 'menu': menu, 'title': 'Добавление поста'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

class ShowPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


#def show_post(request, post_slug):
#    post = get_object_or_404(Post, slug=post_slug)
#
#    context = {
#        'post': post,
#        'menu': menu,
#        'title': post.title,
#        'cat_selected': post.cat.slug,
#    }
#
#    return render(request, 'blog/post.html', context=context)

#def show_category(request, cat_slug):
#    posts = Post.objects.filter(cat__slug=cat_slug)
#
#    context = {
#        'posts': posts,
#        'menu': menu,
#        'title': 'Отображение по категориям',
#        'cat_selected': cat_slug,
#    }
#
#    return render(request, 'blog/index.html', context=context)

class PostCategory(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = self.kwargs['cat_slug']
        return context
    
    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)