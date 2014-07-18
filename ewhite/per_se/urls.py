from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'per_se.views.home', name='home'),
    url(r'^symeq/', include('symeq.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
