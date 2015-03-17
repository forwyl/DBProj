from django.conf.urls import patterns, include, url
from django.contrib import admin

from TWBetter import views


urlpatterns = patterns('',
    # Examples:
    url(r'^welcome/$', views.welcome, name="welcome"),
    url(r'^query_info/$', views.query_info, name="query_info"),
    url(r'^detail/(?P<id>\d+)/$', views.detail, name="detail"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="user_logout"),
    url(r'^add_favorite/(?P<id>\d+)/$', views.add_favorite, name="add_favorite"),
    url(r'^display_favorite/$', views.display_favorite, name="display_favorite"),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)