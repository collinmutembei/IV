from django.db import models
from api.models.user import User


def set_upload_file_path(instance, filename):
    """sets upload directory for users from a derivation of their uuid"""
    user = User.objects.get(username=instance.uploaded_by.username)
    if user.username == "anonymous":
        file_path = "{0}/{1}".format('anonymous', filename)
        return file_path
    random_hex = user.uuid.hex
    file_path = "{0}/{1}".format(random_hex[-20:], filename)
    return file_path


class Image(models.Model):
    """defines image"""
    image = models.ImageField(upload_to=set_upload_file_path)
    uploaded_by = models.ForeignKey(
        User,
        to_field='username',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.image.name
