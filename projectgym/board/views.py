from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
<<<<<<< HEAD
from board.models import Post
=======
from board.models import Board
>>>>>>> f4f00cbac0c7c4b9d5f5a6efa70b728107444103


# Create your views here.


def main(request):
    return render(request, 'board/main.html')


def board_list(request):
<<<<<<< HEAD
    return render(request, 'board/menu.html')

def board_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/board_detail.html', {
        'post': post,
=======
    return render(request, 'board/board_list.html',{
        'board_list': Board.objects.all(),

>>>>>>> f4f00cbac0c7c4b9d5f5a6efa70b728107444103
    })