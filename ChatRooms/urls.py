from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ChatRooms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/', 'Chat.views.main'),
    url(r'^register/', 'Chat.views.register'),
    url(r'^register_check/', 'Chat.views.register_check'),
    url(r'^login_check/', 'Chat.views.login_check'),

    url(r'^admin/', include(admin.site.urls)),
)
