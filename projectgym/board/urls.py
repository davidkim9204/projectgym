from django.conf.urls import url
from . import views



urlpatterns =[
    url(r'^$', views.main),
    url(r'^list$', views.board_list),
    #url(r'^list$', views.board_new),
    url(r'^(?P<pk>\d+)/$', views.board_detail, name = 'board_detail'),
    #url(r'^(?P<board_slug>[-\w]+)/$', views.board_detail, name = 'board_detail'),
    url(r'^(?P<board_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<board_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^(?P<board_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]