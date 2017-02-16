from django.contrib import admin
<<<<<<< HEAD
from .models import Post
# Register your models here.
admin.site.register(Post)
=======
from board.models import Board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    search_fields =  ['title']
    list_display = ['title', 'created_at','updated_at']
    list_display_links = ['title']
    list_filter=['created_at']

admin.site.register(Board,BoardAdmin)
>>>>>>> f4f00cbac0c7c4b9d5f5a6efa70b728107444103
