from django.test import TestCase
from .models import Receipt

# Create your tests here.

class URLTest(TestCase):

    def test_homepage(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_homepage_FAILURE(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,400)

