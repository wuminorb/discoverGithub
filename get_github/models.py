from django.db import models


class GithubUser(models.Model):
    blog = models.URLField
    company = models.TextField
    create_at = models.DateTimeField
    emile = models.EmailField
    following = models.ManyToManyField("self", symmetrical=False)
    hireable = models.NullBooleanField
    location = models.TextField
    login = models.TextField
    name = models.TextField
    public_repo_num = models.IntegerField
    update_at = models.DateTimeField


class GithubRepo(models.Model):
    full_name = models.TextField
    description = models.TextField
    stargazers_count = models.IntegerField
    watchers_count = models.IntegerField
    forks_count = models.IntegerField
    create_at = models.DateTimeField
    pushed_at = models.DateTimeField
