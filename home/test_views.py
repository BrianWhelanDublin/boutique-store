from django.test import TestCase


class TestDjango(TestCase):

    def test_this_works(self):
        self.assertEqual(1, 1)
    
    def test_home_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
