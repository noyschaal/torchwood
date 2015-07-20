"""mindframe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from mindframe import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', "mindframe.views.login", name='login'),
    url(r'^auth/$', "mindframe.views.auth_view"),
    url(r'^logout/$', "mindframe.views.logout"),

    url(r'^accounts/invalid/$', "mindframe.views.invalid_login"),

    url(r'^createUser/$', "mindframe.views.register_user"),
    url(r'^createTopic/$', "mindframe.views.createTopic"),
    url(r'^createEntry/$', "mindframe.views.createEntry"),

    #url(r'^users/', views.users, name='users'),
    url(r'^topic/(?P<topic_id>\d+)/$', "mindframe.views.topic", name='topic'),
    url(r'^$', "mindframe.views.index", name='index'),
    url(r'^index/$', "mindframe.views.index", name='index'),
    #url(r'^createTopic/', views.createTopic, name='createTopic'),
    #url(r'^createGroup/', views.createGroup, name='createGroup'),
]
