from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


article_list=ArticleViewSet.as_view({
    'get':'list',
    'post':'create'
})

article_detail=ArticleViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})
article_highlight=ArticleViewSet.as_view({
    'get':'highlight'
})


user_list=UserViewSet.as_view({
    'get':'list'
})

user_detail=UserViewSet.as_view({
    'get':'retrieve',
})

#extends from '' 
urlpatterns = [
    path('',api_root),
    # path('article/', ArticleListView.as_view(),name='article-list'),  
    # path('article/<int:pk>/',ArticleDetailView.as_view(),name='article-detail'),
    # path('article/<int:pk>/body',ArticleHighlight.as_view(),name='article-highlight'),
    # path('user/',UserList.as_view(),name='user-list'),
    # path('user/<int:pk>/',UserDetail.as_view(),name='user-detail'),

    path('article/', article_list, name='article-list'),  
    path('article/<int:pk>/',article_detail, name='article-detail'),
    path('article/<int:pk>/body',article_highlight, name='article-highlight'),
    path('user/',user_list, name='user-list'),
    path('user/<int:pk>/',user_detail,name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)