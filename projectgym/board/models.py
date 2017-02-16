from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length = 20, verbose_name='이름')
    photo = models.ImageField(upload_to='board/post/%pk', blank=True, verbose_name='사진')
    guide = models.TextField(verbose_name='하는 법')
    effect = models.TextField(verbose_name='효과')
    link = models.URLField(verbose_name='동영상 링크')

    def __str__(self):
        return self.name