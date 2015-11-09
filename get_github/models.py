from django.db import models


class GithubUser(models.Model):
    blog = models.URLField(null=True)
    company = models.CharField(null=True, max_length=255)
    create_at = models.DateTimeField(null=True)
    emile = models.EmailField(null=True)
    following = models.ManyToManyField("self", symmetrical=False)
    hireable = models.NullBooleanField(null=True)
    location = models.CharField(null=True, max_length=255)
    login = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(null=True, max_length=255)
    public_repo_num = models.IntegerField(default=0)
    update_at = models.DateTimeField(null=True)


class GithubRepo(models.Model):
    full_name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(null=True)
    stargazers_count = models.IntegerField(default=0)
    watchers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)
    create_at = models.DateTimeField()
    pushed_at = models.DateTimeField()
