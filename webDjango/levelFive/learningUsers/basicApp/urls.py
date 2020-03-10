from django.urls import path, re_path
from basicApp import views

app_name = 'basicApp'

urlpatterns = [
    re_path(r'^register', views.register, name='register'),
    re_path(r'^userLogin', views.userLogin, name='userLogin'),
    ]
