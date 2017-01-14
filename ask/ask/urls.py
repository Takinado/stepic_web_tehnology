# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa.views import test, popular, question_details, new
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', question_list_all, name='question-list-all'),
    url(r'^$', new, name='index'),
    url(r'^login/', test, name='login'),
    url(r'^logout/', test, name='logout'),
    url(r'^signup/', test),
    url(r'^question/(?P<pk>\d+)/$', question_details, name='question-details'),
    url(r'^ask/', test),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', new, name='new'),

    url(r'^admin/', include(admin.site.urls)),
)
