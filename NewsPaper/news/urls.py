from django.urls import path
from .views import (
    PostList, PostDetail,
    Search,
    NewsCreate,
    NewsEdit,
    NewsDelete, ArticleCreate, ArticleEdit, ArticleDelete, CategoryListView, subscribe, subscriptions
)


urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('create/', NewsCreate.as_view(), name='create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='post_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
