from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemas.views import sitemap
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','techBlog.views.index',name='index'),
    url(r'^(?P<slug>[\w\-]+)/$','techBlog.views.post',name='post'),
    url(r'^blog/trending/$','techBlog.views.trending',name='trending'),
    url(r'^blog/search/$','techBlog.views.search',name='search'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
)
