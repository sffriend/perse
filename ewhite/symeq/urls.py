from django.conf.urls import patterns, url

from symeq import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)

