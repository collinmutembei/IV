from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import URLValidator
from django.db import models, transaction
import uuid

from . import custom_model_field


class AccountManager(BaseUserManager):
    """Manager class for the custom user model."""

    class Meta:
        app_label = 'api'

    def create_user(self, email, password=None, **kwargs):
        """Override the default create_user() method."""

        if not email:
            raise ValueError('Users must have a valid email address.')

        account = self.model(
            email=self.normalize_email(email),
            profile=kwargs.get('user')
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        """Override the default create_superuser() method."""

        account = self.create_user(email, password, **kwargs)
        account.is_admin = True
        account.save()
        return account


class UserProfile(models.Model):
    """model for the user"""

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    username = custom_model_field.CharFieldCaseInsensitive(
        max_length=70,
        unique=True
    )
    avater_url = models.TextField(validators=[URLValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'api'

    def __unicode__(self):
        return self.username

    @classmethod
    @transaction.atomic
    def create_userprofile(cls, **kwargs):
        """Method that creates a userprofile."""

        user = UserProfile.objects.create(
            username=kwargs.get('username'),
        )

        user_profile = User.objects.create_user(
            kwargs.get('email'),
            password=kwargs.get('password'),
            user=user
        )
        return user_profile


class User(AbstractBaseUser):
    """This model is to contain user related data"""

    email = custom_model_field.EmailFieldCaseInsensitive(unique=True)
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    profile = models.ForeignKey(UserProfile, related_name="profile")
    objects = AccountManager()
    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'api'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        """Return user's full names."""

        return '{0} {1} '.format(self.first_name, self.last_name)

    def get_email(self):
        """Return user email."""

        return self.email
