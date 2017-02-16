from django.db import models
from django.utils import timezone

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 50)
    photo = models.ImageField()
    category = models.CharField(max_length = 20)
    instruction = models.TextField()
    outcomes = models.TextField()
    links = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.title