from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^github/', include('cache_github.urls')),
)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
