from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from app.utils import *
from .forms import *


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация', cat_selected='')
        return dict(list(context.items())+list(c_def.items()))



def login(request):
    return HttpResponse('Авторизация')

def register(request):
    return HttpResponse('Регистрация')

def logout(request):
    return HttpResponse('Выход')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')