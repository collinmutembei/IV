from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.core import validators
from django.db import models
import uuid
import re


class UserManager(BaseUserManager):
    """Manager class for the custom user model."""

    class Meta:
        app_label = 'api'

    def create_user(
        self,
        username,
        password=None,
    ):
        """Override the default create_user() method."""

        account = self.model(username=username)
        account.set_password(password)
        account.save()
        return account

    def create_superuser(
        self,
        username,
        password=None,
    ):
        """Override the default create_superuser() method."""

        account = self.create_user(username, password)
        account.is_superuser = True
        account.save()
        return account


class User(AbstractBaseUser, PermissionsMixin):
    """Model defining the user"""

    class Meta:
        app_label = 'api'

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(
        max_length=254,
        unique=True,
        validators=[validators.RegexValidator(
            re.compile('^[\w.@+-]+$'),
            'Enter a valid username.',
            'invalid'
        )]
    )
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def get_short_name(self):
        return self.username
