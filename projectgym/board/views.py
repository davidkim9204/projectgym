from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from board.models import Board


# Create your views here.


def main(request):
    return render(request, 'board/main.html')


def board_list(request):
    return render(request, 'board/board_list.html',{
        'board_list': Board.objects.all(),

    })