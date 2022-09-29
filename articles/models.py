from django.db import models

# Create your models here.
class Article(models.Models): #상속
    # id 는 자동으로 만들어진다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

