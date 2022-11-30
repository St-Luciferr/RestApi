from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from .models import Article
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework import status, generics, permissions
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.decorators import api_view


class ArticleListView(APIView):
    '''
    List all Articles, or create a new Article.
    '''
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        articles=Article.objects.all()
        serializer=ArticleSerializers(articles,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=ArticleSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetailView(APIView):
    '''
    Retrieve, update or delete a Article instance.
    '''
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get_object(self, pk):
        '''
        find an article
        '''
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        retrieve detail of an article
        '''
        article=self.get_object(pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        '''
        update an article
        '''
        article=self.get_object(pk)
        serializer = ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        '''delete an article'''
        article=self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Using generic view class
class UserList(generics.ListAPIView):
    '''
    Lists all the Users
    '''
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveAPIView):
    '''
    Shows the detail of requested User
    '''
    queryset=User.objects.all()
    serializer_class=UserSerializer

#function based view for article list
'''
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
'''


#function based view for article detail
'''
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
'''