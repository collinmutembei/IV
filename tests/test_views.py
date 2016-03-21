from django.test import TestCase


class PheditViewTestCase(TestCase):
    """define tests for views"""

    def test_dashboard_page_view(self):
        """test behaviour on accessing app dashboard"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'PHEDIT')

    def test_landing_page_view(self):
        """test accessing the landing page"""
        resp = self.client.get('/xyzabcd')
        self.assertEqual(resp.status_code, 404)
