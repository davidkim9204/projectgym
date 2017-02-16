from django.contrib import admin
from board.models import Board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    search_fields =  ['title']
    list_display = ['title', 'category','created_at']
    list_display_links = ['title']
    list_filter=['created_at']

admin.site.register(Board,BoardAdmin)