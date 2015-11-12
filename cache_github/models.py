from django.db import models
from django.utils.timezone import make_aware
from cache_github.connect import G


class GithubUser(models.Model):
    avatar = models.URLField(null=True)
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

    def __str__(self):
        return self.login

    def get_data(self, data=None):
        if data:
            self.data = data

        if not hasattr(self, 'data'):
            self.data = G.get_user(self.login)

        return self.data

    def refresh_from_github(self, data=None):
        self.data = self.get_data(data)
        self.avatar = self.data.avatar_url
        self.blog = self.data.blog
        self.company = self.data.company
        self.create_at = make_aware(self.data.created_at)
        self.emile = self.data.email
        self.hireable = self.data.hireable
        self.location = self.data.location
        self.name = self.data.name
        self.public_repo_num = self.data.public_repos
        self.update_at = make_aware(self.data.updated_at)
        self.followers_count = self.data.followers
        self.following_count = self.data.following
        self.save()

    def refresh_following(self, data=None, force=False):
        self.data = self.get_data(data)
        followings = self.data.get_following()
        if not force:
            followings = followings.get_page(0)

        for following in followings:
            self.following.add(get_user_from_db(following.login))

    def refresh_starred(self, data=None, force=False):
        self.data = self.get_data(data)
        starred_repose = self.data.get_starred()
        if not force:
            starred_repose = starred_repose.get_page(0)

        for starred in starred_repose:
            repo = GithubRepo()
            repo.refresh_from_github(starred)
            self.starred.add(repo)


class GithubRepo(models.Model):
    full_name = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(null=True)
    stargazers_count = models.IntegerField(default=0)
    watchers_count = models.IntegerField(default=0)
    forks_count = models.IntegerField(default=0)
    create_at = models.DateTimeField(null=True)
    pushed_at = models.DateTimeField(null=True)
    stargazers = models.ManyToManyField(GithubUser, related_name='starred')

    def __str__(self):
        return self.full_name

    def get_data(self, data=None):
        if data:
            self.data = data

        if not hasattr(self, 'data'):
            self.data = G.get_repo(self.full_name)

        return self.data

    def refresh_from_github(self, data=None):
        self.data = self.get_data(data)
        self.full_name = self.data.full_name
        self.forks_count = self.data.forks_count
        self.create_at = make_aware(self.data.created_at)
        self.description = self.data.description
        self.pushed_at = make_aware(self.data.pushed_at)
        self.stargazers_count = self.data.stargazers_count
        self.watchers_count = self.data.watchers_count
        self.save()


def get_user_from_db(login):
    query_set = GithubUser.objects.filter(login=login)
    if query_set.exists():
        return query_set.first()
    else:
        user = GithubUser()
        user.login = login
        user.save()
        return user
