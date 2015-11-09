from django.db import models
from get_github.connect import G


class GithubUser(models.Model):
    blog = models.URLField(null=True)
    company = models.CharField(null=True, max_length=255)
    create_at = models.DateTimeField(null=True)
    emile = models.EmailField(null=True)
    following_count = models.IntegerField(default=0)
    followers_count = models.IntegerField(default=0)
    following = models.ManyToManyField("self", symmetrical=False)
    hireable = models.NullBooleanField(null=True)
    location = models.CharField(null=True, max_length=255)
    login = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(null=True, max_length=255)
    public_repo_num = models.IntegerField(default=0)
    update_at = models.DateTimeField(null=True)

    def refresh_from_github(self):
        user_data = G.get_user(self.login)
        self.blog = user_data.blog
        self.company = user_data.company
        self.create_at = user_data.created_at
        self.emile = user_data.email
        self.hireable = user_data.hireable
        self.location = user_data.location
        self.name = user_data.name
        self.public_repo_num = user_data.public_repos
        self.update_at = user_data.updated_at
        self.followers_count = user_data.followers
        self.following_count = user_data.following
        self.user_data = user_data

    def refresh_following(self):
        if not self.user_data:
            self.user_data = G.get_user(self.login)

        followings = self.user_data.get_following()
        for following in followings:
            query_set = GithubUser.objects.filter(login=following.login)
            if query_set.exists():
                following_user = query_set.first()
            else:
                following_user = GithubUser()
                following_user.login = following.login
                following_user.save()
            self.following.add(following_user)


class GithubRepo(models.Model):
    full_name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(null=True)
    stargazers_count = models.IntegerField(default=0)
    watchers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)
    create_at = models.DateTimeField()
    pushed_at = models.DateTimeField()
