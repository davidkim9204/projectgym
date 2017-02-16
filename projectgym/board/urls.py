from django.conf.urls import url
from . import views



urlpatterns =[
    url(r'^$', views.main),
    url(r'^list/$', views.board_list, name= 'board_list'),
    #url(r'^list$', views.board_new),
    url(r'^(?P<pk>\d+)/$', views.board_detail, name = 'board_detail'),
    #url(r'^(?P<board_slug>[-\w]+)/$', views.board_detail, name = 'board_detail'),
]