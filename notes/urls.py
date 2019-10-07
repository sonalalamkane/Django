from django.conf.urls import url
from django.urls import include

from .views import index_view, add_note, add_tag, search

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^addnote/', add_note, name='addnote'),
    url(r'^addtag/', add_tag, name='addtag'),
    url(r'^search/', search, name='search')
]
