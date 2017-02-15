from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


def board_list(request):
    return render(request, 'board/menu.html')