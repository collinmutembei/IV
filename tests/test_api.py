from api.models.user import User
from rest_framework.test import APITestCase, APIClient
import os


class PheditAPITestCase(APITestCase):
    """defines tests for the api"""

    def setUp(self):
        """initializes the test client and test users"""
        self.client = APIClient()
        self.anonymous_user = User(username='anonymous')
        self.anonymous_user.set_password('dbfdu76&mHN')
        self.anonymous_user.save()
        self.anonymous_user = User(username='testuser')
        self.anonymous_user.set_password('ncvsN809ibkj!*HJ2612J')
        self.anonymous_user.save()

    def test_api_endpoint(self):
        """test for api endpoint"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data['users'],
            'http://testserver/api/users/'
        )
        self.assertEqual(
            response.data['images'],
            'http://testserver/api/images/'
        )

    def test_api_users_endpoint(self):
        """test for api users endpoint"""
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_creating_api_user_endpoint(self):
        """test for creating a new user"""
        response = self.client.post(
            '/api/users/',
            {'username': 'anothertestuser', 'password': 'test'}
        )
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 201)

    def test_getting_api_user_endpoint(self):
        """test for getting users"""
        self.client.post(
            '/api/users/',
            {'username': 'anotheruser', 'password': 'test'}
        )
        response = self.client.get('/api/users/anotheruser/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data['username'],
            'anotheruser'
        )

    def test_api_images_endpoint(self):
        """test for getting images"""
        response = self.client.get('/api/images/')
        self.assertEqual(response.status_code, 200)

    def test_uploading_image_to_images_api_endpoint_as_anonymous_user(self):
        """test for creating a new image"""
        path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path, 'hashtag.jpg'), "rb") as image:
            response = self.client.post(
                '/api/images/',
                {'image': image},
                format='multipart'
            )
        self.assertEqual(response.status_code, 201)

        # test uploader
        response = self.client.get('/api/images/')
        self.assertEqual(
            response.data[0].get('uploaded_by'),
            'anonymous'
        )
        self.assertEqual(response.status_code, 200)

    def test_uploading_image_to_images_api_endpoint_as_other_user(self):
        """test for creating a new image as logged-in user"""
        self.client.login(
            username='testuser',
            password='ncvsN809ibkj!*HJ2612J'
        )

        path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path, 'hashtag.jpg'), "rb") as image:
            response = self.client.post(
                '/api/images/',
                {'image': image},
                format='multipart'
            )
        self.assertEqual(response.status_code, 201)

        # test uploaded by other user
        response = self.client.get('/api/images/')
        self.assertEqual(
            response.data[0].get('uploaded_by'),
            'testuser'
        )
        self.assertEqual(response.status_code, 200)

        self.client.logout()
