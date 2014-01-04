from django.conf.urls import patterns, url

from reports import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'bandwidth$', views.bandwidth, name='bandwidth'),
    url(r'graph$', views.graph, name='graph'))
