from django.db import models


class CharFieldCaseInsensitive(models.CharField):
    """Custom model field class for CharField."""

    def get_db_prep_save(self, value, connection):
        """Modify CharField before saving to database.

        This method ensures the uniqueness of values in a model field by
        enforcing the use of lowercase for all entries made in CharFields.
        This is meant to cater for case insensitivity in databases such as
        PostgreSQL.
        """
        if value is not None:
            value = value.lower()

            return value


class EmailFieldCaseInsensitive(models.EmailField):
    """Custom model field class for EmailField."""

    def get_db_prep_save(self, value, connection):
        """Modify EmailField before saving to database.

        This method ensures the uniqueness of values in a model field by
        enforcing the use of lowercase for all entries made in EmailFields.
        This is meant to cater for case insensitivity in databases such as
        PostgreSQL.
        """
        if value is not None:
            value = value.lower()

            return value
