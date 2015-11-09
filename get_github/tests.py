from django.test import TestCase
from get_github.connect import G
from get_github.models import GithubUser
import get_github.views as views


class FindMethodTests(TestCase):
    def test_refresh_user(self):
        views.refresh_user('wuminorb')
        self.assertEqual(GithubUser.objects.count(), 1)
