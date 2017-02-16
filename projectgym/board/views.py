from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from board.models import Board


# Create your views here.


def main(request):
    return render(request, 'board/main.html')


def board_list(request):
    qs = Board.objects.all()

    category = request.GET.get('category', '')
    if category:
        qs = qs.filter(category=category)
    return render(request, 'board/board_list.html',{
        'board_list': qs,
    })

def board_new(request):
    return render(request, 'board/board_form.html', {
        'form': form,
    })

def board_detail(request, pk):
    board = get_object_or_404(Board, pk = pk)
    return render(request, 'board/board_detail.html', {
        'board' : board
    })