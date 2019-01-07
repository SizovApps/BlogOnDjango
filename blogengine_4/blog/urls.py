from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/str:<slug>/', PostDetail.as_view(), name='post_detail_url'),
    # "<slug>" создает строковую переменную, которая называется slug. Мы используем ее, что бы получить slug,
    # который будет использоваться в 'views.py', что бы найти соответствующий пост.
    # Поле 'name' используется в html файлах для создания ссылок на эти страницы.
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),

]