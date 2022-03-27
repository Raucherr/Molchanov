from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    # path('tag/')
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url'),

]