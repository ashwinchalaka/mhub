from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^bio$', views.bio, name='bio'),
    url(r'^search$', views.search, name='search'),
]