from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, SearchList
from . import views


urlpatterns = [
   path('news/', PostList.as_view(), name='post_list'),
   path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/',  PostCreate.as_view(), name='create_post'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('news/search/', SearchList.as_view(), name='news_search'),
]