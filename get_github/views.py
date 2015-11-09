from django.shortcuts import render
from .models import GithubUser


def add_user(login):
    user = GithubUser()
    user.login = login
    user.refresh_from_github()
    user.save()
    user.refresh_following()
