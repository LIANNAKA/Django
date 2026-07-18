from django.test import TestCase # this is used we are using a database
from django.test import SimpleTestCase # since we do not have a database for now we are using SimpleTestCase
# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
