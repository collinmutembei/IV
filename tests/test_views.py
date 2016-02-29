from django.test import TestCase


class PheditViewTestCase(TestCase):
    def test_landing_page_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'PHEDIT')

    def test_dashboard_view_when_not_authenticated(self):
        resp = self.client.get('/dashboard/')
        self.assertEqual(resp.status_code, 302)
