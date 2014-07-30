from django.conf.urls import patterns, url

from per import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^symbols/$', views.symbols, name='symbols'),
    url(r'^equations/$', views.equations, name='equations'),
    url(r'^sections/$', views.sections, name='section'),
    url(r'^exercises/$', views.exercises, name='exercises'),
    url(r'^symbols/(?P<per_id>\d+)/$', views.symDetail, name='symDetail'),
    url(r'^equations/(?P<per_id>\d+)/$', views.eqnDetail, name='eqnDetail'),
    url(r'^sections/(?P<per_id>\d+)/$', views.secDetail, name='secDetail'),
    url(r'^exercises/(?P<per_id>\d+)/$', views.excDetail, name='excDetail'),
    url(r'^exclist/$', views.exclist, name='exclist'),
)