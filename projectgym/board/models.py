from django.db import models
from django.utils import timezone

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 50, unique = True)
    slug=models.SlugField(allow_unicode=True)
    photo = models.ImageField(blank= True)
    category = models.CharField(max_length=1,
        choices=(
            ('1','가슴'),('2','등'),('3','복근'),('4','어깨'),('5','유산소'),('6','하체')
        ),
        default = '5')
    instruction = models.TextField()
    outcomes = models.TextField()
    links = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title
