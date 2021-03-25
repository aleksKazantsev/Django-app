from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index), 
    path('cats/<int:catid>/', categories),
]