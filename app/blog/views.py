from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


#menu = [{'title': "О сайте", 'url_name': 'about'},
#        {'title': "Добавить статью", 'url_name': 'add_post'},
#        {'title': "Обратная связь", 'url_name': 'contact'},
#        {'title': "Войти", 'url_name': 'login'}
#]

class BlogHome(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', cat_selected=0)
        #context['menu'] = menu
        #context['title'] = 'Главная страница'
        #context['cat_selected'] = 
        #context = dict(list(context.items())+list(c_def.items()))
        return dict(list(context.items())+list(c_def.items()))
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpost.html'
    success_url = reverse_lazy('home')
    #login_url = '/admin/'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление поста')
        #context['menu'] = menu
        #context['title'] = 'Добавление поста'
        #return context
        return dict(list(context.items())+list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        #context['menu'] = menu
        #context['title'] = context['post']
        #return context
        return dict(list(context.items())+list(c_def.items()))


class PostCategory(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat), cat_selected=self.kwargs['cat_slug'])
        #context['menu'] = menu
        #context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        #context['cat_selected'] = self.kwargs['cat_slug']
        #return context
        return dict(list(context.items())+list(c_def.items()))
    
    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    
def about(request):
    return render(request, 'blog/about.html', {'menu': menu, 'title': 'О сайте'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
