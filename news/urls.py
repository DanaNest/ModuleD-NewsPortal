from django.urls import path
from .views import (
    PostList, PostDetail,
    Search,
    NewsCreate,
    NewsEdit,
    NewsDelete, ArticleCreate, ArticleEdit, ArticleDelete,
)


# urlpatterns = [
#     path('news/', views.PostList.as_view(), name='news_list'),
#     path('news/<int:pk>', views.PostDetail.as_view(), name='news_detail'),
#     path('news/create/', views.NewsCreate.as_view(), name='news_create'),
#
#     path('article/', views.ArticleList.as_view(), name='article_list'),
#     path('article/<int:pk>', views.ArticleDetail.as_view(), name='article_detail'),
#     path('article/create/', views.ArticleCreate.as_view(), name='article_create'),
# ]

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>/', PostDetail.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('create/', NewsCreate.as_view(), name='create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),

]
