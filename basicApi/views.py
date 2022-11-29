from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def article_list(request,format=None):
    if request.method=='GET':
        articles=Article.objects.all()
        serializer=ArticleSerializers(articles,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk,format=None):
    """
    Retrieve, update or delete an article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)