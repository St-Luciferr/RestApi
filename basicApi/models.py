from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey('auth.User',related_name='articles',on_delete=models.CASCADE)
    email=models.EmailField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()

    def __str__(self):
        return self.title
