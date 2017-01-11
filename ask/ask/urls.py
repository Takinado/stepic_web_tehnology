from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa.views import test
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<pk>\d+/$)', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test),

    url(r'^admin/', include(admin.site.urls)),
)
