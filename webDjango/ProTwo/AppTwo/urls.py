from django.conf.urls import url,include
from AppTwo import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]
