from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('article/', article_list,name='list'),  
    path('article/<int:pk>/',article_detail,name='detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)