from django.conf.urls import patterns, url

from files import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # FIXME do some basic validation here, more in view
    url(r'^(?P<path>.+)$', views.index, name='index'))
