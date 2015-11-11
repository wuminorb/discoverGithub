from django.db import models


class AlsoLikeRepo(models.Model):
    base_repo = models.ForeignKey('cache_github.GithubRepo', related_name='also_likes')
    like_repo = models.ForeignKey('cache_github.GithubRepo')
    weight = models.IntegerField(default=0)
