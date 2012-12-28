from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from ltblog.feed import LatestFeed
from ltblog.sitemap import BlogSitemap

admin.autodiscover()

urlpatterns = patterns('ltblog.views',
    # Examples:
    # url(r'^$', 'liteblog.views.home', name='home'),
    # url(r'^liteblog/', include('liteblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'index'),
    url(r'^blog/(?P<entry_id>\d+)/$', 'entry', name='ltblog_entry'),
    url(r'^category/(?P<category_id>\d+)/$', 'category_entry_list'),
    url(r'^archives/(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'archives_list'),
    url(r'^about/$', 'about'),
    url(r'^search/$', 'search'),

)
sitemaps = {'blog' :BlogSitemap}

urlpatterns += patterns('',

    url(r'^feed/$', LatestFeed()),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps' : sitemaps}),

    url(r'^login/', 'ltblog.views.loginview'),
    url(r'^auth/', 'ltblog.views.auth_and_login'),
    url(r'^fileupload/$', 'ltblog.views.uploadfile', name='list'),
)
