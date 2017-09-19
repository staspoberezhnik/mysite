from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name='home'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<id>\d+)/addcomment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='edit_post'),
    url(r'^user_list/$', views.users_list, name='users_list'),
    url(r'^(?P<id>\d+)/user_post_list/$', views.user_post_list, name='user_post_list'),
    url(r'^(?P<id>\d+)/user_comments_list/$', views.user_comments_list, name='user_comments_list'),
    url(r'^post_by_tags/(?P<tag>[-\w]+)/$', views.post_by_tags, name='post_by_tags'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete_post'),


]
