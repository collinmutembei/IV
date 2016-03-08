from django.db import models
from api.models.user import User
import requests
import io
import os
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def set_upload_file_path(instance, filename):
    """sets upload directory for users from a derivation of their uuid"""
    user = User.objects.get(username=instance.phedited_by.username)
    if user.username == "anonymous":
        file_path = "{0}/phedited/{1}".format('anonymous', filename)
        return file_path
    random_hex = user.uuid.hex
    file_path = "{0}/phedited/{1}".format(random_hex[-20:], filename)
    return file_path


class PheditedImage(models.Model):
    """defines phedited image"""
    original_image = models.URLField()
    phedited_image = models.ImageField(upload_to=set_upload_file_path)
    phedited_by = models.ForeignKey(
        User,
        to_field='username',
        on_delete=models.CASCADE
    )
    phedited_at = models.DateTimeField(auto_now=True)
    effects = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        if self.original_image:
            image_request = requests.get(self.original_image)
            image_bytes = io.BytesIO(image_request.content)
            image = Image.open(image_bytes)
            rotated_image = image.rotate(180)
            edited_image = io.BytesIO()
            rotated_image.save(edited_image, format=image.format)
            filename = os.path.basename(self.original_image)
            edited_file = InMemoryUploadedFile(
                edited_image,
                None,
                filename,
                'image/jpeg',
                edited_image.tell,
                None
            )
            self.phedited_image.save(filename, edited_file, save=False)
        super(PheditedImage, self).save(*args, **kwargs)
