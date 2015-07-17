from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /alumni/
    url(r'^$', views.index, name='index'),
    # ex: /alumni/dataviz
    url(r'^dataviz/$', views.dataviz, name='dataviz'),
    # ex: /alumni/new
    url(r'^new/$', views.new, name='new'),
    # ex: /alumni/5/
    url(r'^(?P<name_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /alumni/5/information/
    # url(r'^(?P<name_id>[0-9]+)/information/$', views.information, name='information'),
]