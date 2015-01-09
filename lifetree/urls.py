from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lifetree.views.home', name='home'),
    url(r'^$', 'xp.views.xpview'),

    url(r'^admin/', include(admin.site.urls)),
)
