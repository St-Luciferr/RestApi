from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('article/', ArticleListView.as_view(),name='list'),  
    path('article/<int:pk>/',ArticleDetailView.as_view(),name='detail'),
    path('user/',UserList.as_view(),name='UserList'),
    path('user/<int:pk>/',UserDetail.as_view(),name='UserDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)