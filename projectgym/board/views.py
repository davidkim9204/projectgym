from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from board.models import Post


# Create your views here.


def board_list(request):
    return render(request, 'board/menu.html')

def board_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/board_detail.html', {
        'post': post,
    })