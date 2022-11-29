from rest_framework import serializers
from basicApi.models import Article

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id', 'title', 'author' ,'email']




    # create and return new article instance from validated data



