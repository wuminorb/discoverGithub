from django.test import TestCase
from get_github.connect import G
from get_github.models import GithubUser
import get_github.views as views


class FindMethodTests(TestCase):
    def test_find_following(self):
        views.add_user('wuminorb')
        following = G.get_user('wuminorb').following
        self.assertEqual(GithubUser.objects.count(), following+1)
