from django.test import TestCase
from api.models import phedited, user
import os
from PIL import Image


class ModelsTestCase(TestCase):
    """define tests for models
    """
    def setUp(self):
        """initializes data to be used in testing
        """
        self.TEST_DIR = os.path.dirname(os.path.abspath(__file__))
        self.image_filename = [file for file in os.listdir(self.TEST_DIR) if file.endswith('jpg')][0]
        self.user = user.User(username="uploader", password="sdHRjku453485643")
        self.user.save()
        self.anonymous_user = user.User(username='anonymous')
        self.anonymous_user.set_password('jvafGJ8342*!')
        self.anonymous_user.save()

    def test_upload_path(self):
        """test for the directory where uploaded image is saved
        """
        # for anonymous user
        self.image_being_edited = phedited.PheditedImage(phedited_by=self.anonymous_user)
        self.image_being_edited.effects = ['BLUR']
        anon_upload_path = phedited.set_upload_file_path(self.image_being_edited, self.image_filename)
        self.assertEqual(anon_upload_path, 'anonymous/phedited/BLUR_hashtag.jpg')

        # for logged in user
        self.image_being_edited = phedited.PheditedImage(phedited_by=self.user)
        self.image_being_edited.effects = ['BLUR']
        user_hex = self.user.uuid.hex[-20:]
        user_upload_path = phedited.set_upload_file_path(self.image_being_edited, self.image_filename)
        self.assertEqual(user_upload_path, '{0}/phedited/BLUR_hashtag.jpg'.format(user_hex))

    def test_apply_effect(self):
        """test applying effect on image
        """
        self.image_before = Image.open(self.TEST_DIR + '/' + self.image_filename)
        self.effects = ['HULK']
        self.image_after = phedited.apply_effects(self.image_before, self.effects)
        self.image_before_pixel = self.image_before.getpixel((1, 1))
        self.image_after_pixel = self.image_after.getpixel((1, 1))
        self.assertNotEqual(self.image_before_pixel, self.image_after_pixel)

    def test_user_creation(self):
        """test creating a normal user and superuser
        """
        # normal user
        self.another_user = user.User.objects.create_user(
            username="dj-khaled",
            password="another1"
        )
        self.assertEqual(self.another_user.is_superuser, False)
        # for superuser
        self.admin_user = user.User.objects.create_superuser(
            username="superuser",
            password="another1"
        )
        self.assertEqual(self.admin_user.is_superuser, True)
