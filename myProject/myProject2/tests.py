from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page(self):
        self.assertEqual(2+2, 4)