"""Django models utilities."""

# Django
from django.db import models


class BaseModel(models.Model):
    """Account base model.

    BaseModel acts as an abstract base class from wich every 
    other model in the project will inherit. This class provides
    every table with the following atributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """
    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='Date time on wich the object was created.'
    )  
    modified = models.DateTimeField(
        'modified_at',
        auto_now=True,
        help_text='Date time on wich the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
