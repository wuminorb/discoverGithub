from django.test import TestCase
from cache_github.connect import G
from cache_github.models import GithubUser
import cache_github.views as views


class FindMethodTests(TestCase):
    def test_refresh_user(self):
        views.refresh_user(None, 'wuminorb')
        self.assertEqual(GithubUser.objects.count(), 1)
