from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name='home'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
    url(r'^(?P<id>\d+)/addcomment/$', views.add_comment, name='comment'),
    url(r'^(?P<id>\d+)/addtag/$', views.add_tag, name='tag'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='edit'),
    url(r'^user_list/$', views.users_list, name='users'),
    url(r'^(?P<id>\d+)/user_post_list/$', views.user_post_list, name='user_post_list'),
    url(r'^(?P<id>\d+)/user_comments_list/$', views.user_comments_list, name='comments_list'),


]
