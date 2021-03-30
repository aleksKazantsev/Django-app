from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout, name='logout'),
]