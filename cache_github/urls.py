from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /github/user/wuminorb
    url(r'^user/(?P<pk>[a-zA-Z0-9_-]+)/$', views.UserDetailView.as_view(), name='user_detail'),
    url(r'^refresh/user/(?P<login>[a-zA-Z0-9_-]+)/$', views.refresh_user, name='refresh_user'),
    url(r'^refresh/user_following/(?P<login>[a-zA-Z0-9_-]+)/$', views.refresh_following, name='refresh_user_following'),
]