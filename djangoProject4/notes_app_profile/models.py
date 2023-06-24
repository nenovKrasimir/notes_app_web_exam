from django.db import models


# Create your models here.
class NotesAppProfile(models.Model):

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=30
    )

    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=30
    )

    age = models.IntegerField(
        blank=False,
        null=False
    )

    image_url = models.URLField(
        blank=False,
        null=False
    )


class NotesAppNote(models.Model):

    title = models.CharField(
        blank=False,
        null=False,
        max_length=30
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    content = models.TextField(
        blank=False,
        null=False,
    )

