from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import generic
from .models import GithubUser, get_user_from_db, GithubRepo


def refresh_user(request, login):
    user = GithubUser()
    user.login = login
    user.refresh_from_github()
    return HttpResponse("success")


def refresh_following(request, login):
    user = get_user_from_db(login)
    user.refresh_following()
    return HttpResponse("success")


def refresh_starred(request, login):
    user = get_user_from_db(login)
    user.refresh_starred()
    return HttpResponse("success")


class UserDetailView(generic.DetailView):
    model = GithubUser
    template_name = 'github/user/detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        try:
            return super(UserDetailView, self).get_object(queryset)
        except Http404:
            pk = self.kwargs.get(self.pk_url_kwarg, None)
            user = GithubUser()
            user.login = pk
            user.refresh_from_github()
            return user


class RepoDetailView(generic.DetailView):
    model = GithubRepo
    template_name = 'github/repo/detail.html'
    context_object_name = 'repo'

    def get_object(self, queryset=None):
        try:
            return super(RepoDetailView, self).get_object(queryset)
        except Http404:
            pk = self.kwargs.get(self.pk_url_kwarg, None)
            repo = GithubRepo()
            repo.full_name = pk
            repo.refresh_from_github()
            return repo
