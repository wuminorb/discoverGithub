from django.db import models


class GithubUser(models.Model):
    blog = models.URLField(null=True)
    company = models.CharField(null=True, max_length=255)
    create_at = models.DateTimeField()
    emile = models.EmailField(null=True)
    following = models.ManyToManyField("self", symmetrical=False)
    hireable = models.NullBooleanField()
    location = models.CharField(null=True, max_length=255)
    login = models.CharField(max_length=255)
    name = models.CharField(null=True, max_length=255)
    public_repo_num = models.IntegerField(default=0)
    update_at = models.DateTimeField()


class GithubRepo(models.Model):
    full_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    stargazers_count = models.IntegerField(default=0)
    watchers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)
    create_at = models.DateTimeField()
    pushed_at = models.DateTimeField()
