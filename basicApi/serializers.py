from rest_framework import serializers
from basicApi.models import Article
from django.contrib.auth.models import User

class ArticleSerializers(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=Article
        fields=['id', 'title', 'author' ,'email', 'body']
    
    # def save(self, **kwargs):
    #     article=Article.objects.create(self.validated_data)



class UserSerializer(serializers.ModelSerializer):
    articles=serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model=User
        fields=['id', 'username', 'articles']



