from django.conf.urls import patterns, include, url

from django.contrib import admin

from per import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'per_se.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

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
    url(r'^secexclist/$', views.SecExc, name='secexclist'),
    url(r'^exclist/results$', views.listResults, name='excListResults'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hair/$', views.hair, name='hair'),
)