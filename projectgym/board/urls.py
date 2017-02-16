from django.conf.urls import url
from . import views



urlpatterns =[
    url(r'^$', views.main),
    url(r'^list$', views.board_list),
<<<<<<< HEAD
    url(r'^list$', views.board_new),
=======
    url(r'^(?P<pk>\d+)/$', views.board_detail, name = 'board_detail')
>>>>>>> 2288924245ad4834cef8adf7a80229658e79b21c
]