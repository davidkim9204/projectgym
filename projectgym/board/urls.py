from django.conf.urls import url
from . import views



urlpatterns =[
    url(r'^$', views.board_list ),
    #url(r'')
]