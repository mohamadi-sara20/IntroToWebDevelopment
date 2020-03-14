from django.urls import re_path
from . import views

app_name='groups'

urlpatterns=[
    re_path(r'^$', views.ListGroup.as_view(), name='all'),
    re_path(r'^news/', views.CreateGroup.as_view, name='create'),
    re_path(r'posts/in/(?P<slug>[-\w]+)/$', views.SignleGroup.as_view(), name='single')
]
