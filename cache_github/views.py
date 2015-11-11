from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import GithubUser, get_user_from_db


def refresh_user(request, login):
    user = GithubUser()
    user.login = login
    user.refresh_from_github()
    return HttpResponse("success")


def refresh_following(request, login):
    user = get_user_from_db(login)
    user.refresh_following()
    return HttpResponse("success")


class UserDetailView(generic.DetailView):
    model = GithubUser
    template_name = 'github/user/detail.html'
    context_object_name = 'user'
