from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('addpost/', AddPost.as_view(), name='add_post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
]