from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^logout/', views.log_out, name='logout'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<id>\d+)/view_profile/$', views.view_profile, name='view_profile'),
    url(r'^(?P<id>\d+)/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<id>\d+)/password/$', views.password_change, name='password_change'),


]
