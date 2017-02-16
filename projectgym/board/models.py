from django.db import models
from django.utils import timezone

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 50)
<<<<<<< HEAD
    photo = models.ImageField(blank= True)
    category = models.CharField(max_length = 20)
=======
    photo = models.ImageField(blank=True)
    category = models.CharField(max_length=1,
        choices=(
            ('c','가슴'),('s','어깨'),('b','등'),('l','하체'),('p','복근'),('a','유산소')
        ),
        default = 'a')
>>>>>>> 95863090f8b02a3b201e93f2da2d2f868a6e2c9c
    instruction = models.TextField()
    outcomes = models.TextField()
    links = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title
