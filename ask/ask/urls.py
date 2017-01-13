# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa.views import test, popular, question_all, new
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', question_all, name='question_all'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<pk>\d+/$)', test),
    url(r'^ask/', test),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', new, name='new'),

    url(r'^admin/', include(admin.site.urls)),
)
