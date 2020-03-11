from django.conf.urls import re_path
from basicApp import views

app_name = 'basicApp'
urlpatterns = [
    re_path(r'^$', views.SchoolListView.as_view(), name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail')

]
