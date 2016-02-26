from api.models.user import User
from rest_framework.test import APITestCase, APIClient
import os


class PheditAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.anonymous_user = User(username='anonymous')
        self.anonymous_user.set_password('dbfdu76&mHN')
        self.anonymous_user.save()

    def test_api_endpoint(self):
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
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_creating_api_user_endpoint(self):
        response = self.client.post(
            '/api/users/',
            {'username': 'testuser', 'password': 'test'}
        )
        self.assertEqual(response.status_code, 201)

    def test_getting_api_user_endpoint(self):
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
        response = self.client.get('/api/images/')
        self.assertEqual(response.status_code, 200)

    def test_uploading_image_to_images_api_endpoint(self):
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
