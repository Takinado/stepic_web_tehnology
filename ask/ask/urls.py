# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa.views import test, popular, question_detail, new, question_ask, question_answer_add
from qa.views import user_singup, user_login, user_logout
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', question_list_all, name='question-list-all'),
    url(r'^$', new, name='index'),
    url(r'^login/', user_login, name='user_login'),
    url(r'^logout/', user_logout, name='user_logout'),
    url(r'^singup/', user_singup, name='user_singup'),
    url(r'^signup/', test),
    url(r'^question/(?P<pk>\d+)/', question_detail, name='question_detail'),
    url(r'^answer/', question_answer_add, name='question_answer'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', new, name='new'),

    url(r'^admin/', include(admin.site.urls)),
)
