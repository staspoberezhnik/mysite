from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^logout/', views.log_out, name='logout'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^register/$', views.register, name='register'),


]
