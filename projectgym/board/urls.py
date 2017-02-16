from django.conf.urls import url
from . import views



urlpatterns =[
<<<<<<< HEAD
    url(r'^$', views.board_list, name='board_list' ),
    url(r'^(?P<pk>\d+)/$', views.board_detail, name = 'board_detail')
=======
    url(r'^$', views.main),
    url(r'^list$', views.board_list),
>>>>>>> f4f00cbac0c7c4b9d5f5a6efa70b728107444103
]