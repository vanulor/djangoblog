from django.test import TestCase
from django.contrib.auth.models import User
from blogging.models import Post


class PostTestCase(TestCase):
    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
