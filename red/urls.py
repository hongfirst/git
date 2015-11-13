"""red URL Configuration

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
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'books.views.start'),
    url(r'^search/$', 'books.views.search'),
    url(r'^detail/$', 'books.views.detail'),
    url(r'^delete/$', 'books.views.delete'),
    url(r'^create/$', 'books.views.create'),
    url(r'^update/$', 'books.views.update'),
    url(r'^author/$', 'books.views.author'),
    url(r'^showall/$', 'books.views.showall'),
]
