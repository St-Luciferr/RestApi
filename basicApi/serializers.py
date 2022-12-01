from rest_framework import serializers
from basicApi.models import Article
from django.contrib.auth.models import User

class ArticleSerializers(serializers.HyperlinkedModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    highlight=serializers.HyperlinkedIdentityField(view_name='article-highlight', format = 'html')
    class Meta:
        model=Article
        fields=['url', 'id', 'title', 'author' ,'email', 'body', 'highlight']
    
    # def save(self, **kwargs):
    #     article=Article.objects.create(self.validated_data)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles=serializers.HyperlinkedRelatedField(many=True, view_name = 'article-detail', read_only=True)

    class Meta:
        model=User
        fields=['url', 'id', 'username', 'articles']



