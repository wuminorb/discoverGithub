from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /github/user/wuminorb
    url(r'^user/(?P<pk>[a-zA-Z0-9]+)/$', views.UserDetailView.as_view(), name='user_detail'),
    url(r'^refresh/user/(?P<login>[a-zA-Z0-9]+)/$', views.refresh_user, name='refresh_user'),
]