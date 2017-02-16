from django.db import models
from django.utils import timezone

# Create your models here.
<<<<<<< HEAD
class Post(models.Model):
    name = models.CharField(max_length = 20, verbose_name='이름')
    photo = models.ImageField(upload_to='board/post/%pk', blank=True, verbose_name='사진')
    guide = models.TextField(verbose_name='하는 법')
    effect = models.TextField(verbose_name='효과')
    link = models.URLField(verbose_name='동영상 링크')

    def __str__(self):
        return self.name
=======

class Board(models.Model):
    title = models.CharField(max_length = 50)
    instruction = models.TextField()
    outcomes = models.TextField()
    links = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title
>>>>>>> f4f00cbac0c7c4b9d5f5a6efa70b728107444103
