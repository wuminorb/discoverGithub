from django.test import TestCase
from recommend import views


class FindMethodTests(TestCase):
    def test_refresh_also_like(self):
        views.refresh_also_like_repo(None, 'ulion/jsonform')
