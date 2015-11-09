from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import GithubUser


def refresh_user(request, login):
    user = GithubUser()
    user.login = login
    user.refresh_from_github()
    user.save()
    return HttpResponse("success")


class UserDetailView(generic.DetailView):
    model = GithubUser
    template_name = 'github/user/detail.html'
    context_object_name = 'user'
