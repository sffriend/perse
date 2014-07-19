from django.conf.urls import patterns, url

from per import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^symbols/$', views.symbols, name='symbols'),
    url(r'^equations/$', views.equations, name='equations'),
    url(r'^symbols/(?P<per_id>\d+)/$', views.symDetail, name='symDetail'),
    url(r'^equations/(?P<per_id>\d+)/$', views.eqnDetail, name='eqnDetail'),
)