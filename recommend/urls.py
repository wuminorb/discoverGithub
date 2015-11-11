from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^refresh/also_like/(?P<full_name>[a-zA-Z0-9_-]+/[.a-zA-Z0-9_-]+)/$', views.refresh_also_like_repo,
        name='refresh_also_like'),
]
