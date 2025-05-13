from django.test import TestCase, Client
from django.urls import reverse

class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_dashboard_accessible(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to HR Dashboard -Pipeline #2")
