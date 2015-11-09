from django.shortcuts import render
from .connect import G
from get_github.dao import save_user, user_exist, update_following
from .models import GithubUser


def add_user(login):
    user_data = G.get_user(login)
    user = save_user(user_data)
    update_following(user_data=user_data, user=user)
