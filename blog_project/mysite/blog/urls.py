from django.urls import path, re_path
from . import views

urlpatterns = [
        re_path(r'^about/$', views.AboutView.as_view(), name='about'),
        re_path(r'^$', views.PostListView.as_view(), name='post-list'),
        re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
        re_path(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
        re_path(r'^post/(?P<pk>\d+)/edit', views.PostUpdateView.as_view(), name='post_update'),

]
