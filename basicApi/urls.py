from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

#extends from '' 

urlpatterns = [
    path('',api_root),
    path('article/', ArticleListView.as_view(),name='article-list'),  
    path('article/<int:pk>/',ArticleDetailView.as_view(),name='article-detail'),
    path('article/<int:pk>/body',ArticleHighlight.as_view(),name='article-highlight'),
    path('user/',UserList.as_view(),name='user-list'),
    path('user/<int:pk>/',UserDetail.as_view(),name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)