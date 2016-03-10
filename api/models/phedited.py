from django.db import models
from api.models.user import User
import requests
import io
import os
from PIL import Image, ImageFilter
from django.core.files.uploadedfile import InMemoryUploadedFile


def set_upload_file_path(instance, filename):
    """sets upload directory for users from a derivation of their uuid"""
    user = User.objects.get(username=instance.phedited_by.username)
    instance.effects.append('')
    effects = "_".join(instance.effects)
    if user.username == "anonymous":
        file_path = "{0}/phedited/{1}{2}".format(
            'anonymous',
            effects,
            filename
        )
        return file_path
    random_hex = user.uuid.hex
    file_path = "{0}/phedited/{1}{2}".format(
        random_hex[-20:],
        effects,
        filename
    )
    return file_path


def apply_effects(image, effects):
    all_effects = {
        'BLUR': ImageFilter.BLUR,
        'CONTOUR': ImageFilter.CONTOUR,
        'EMBOSS': ImageFilter.EMBOSS
    }
    for effect in effects:
        phedited = image.filter(all_effects[effect])
        image = phedited
    return phedited


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
            image_with_effect = apply_effects(image, self.effects)
            edited_image = io.BytesIO()
            image_with_effect.save(edited_image, format=image.format)
            filename = os.path.basename(self.original_image)
            edited_file = InMemoryUploadedFile(
                edited_image,
                None,
                filename,
                'image/jpeg',
                edited_image.tell,
                None
            )

            self.phedited_image.save(
                filename,
                edited_file,
                save=False,
            )
        super(PheditedImage, self).save(*args, **kwargs)
