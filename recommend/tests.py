from django.test import TestCase
from cache_github.models import GithubRepo
from recommend import views


class FindMethodTests(TestCase):
    def test_refresh_also_like(self):
        repo = GithubRepo()
        repo.full_name = 'ulion/jsonform'
        repo.refresh_from_github()
        views.refresh_also_like_repo(None, 'ulion/jsonform')
