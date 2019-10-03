from django.conf.urls import include, url
from django.contrib import admin
from notes.views import index_view

urlpatterns = [
    url(r'^$', index_view, name='index'),
]
