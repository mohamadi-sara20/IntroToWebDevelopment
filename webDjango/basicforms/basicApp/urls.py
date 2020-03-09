from django.conf.urls import url,include
from basicApp import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^', views.form_name, name='form'),
]
