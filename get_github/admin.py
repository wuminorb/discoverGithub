from django.contrib import admin
from .models import GithubUser, GithubRepo


admin.site.register(GithubUser)
admin.site.register(GithubRepo)
