from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import username_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(3, message="Username must be at least 3 chars long!"),
                    username_validator]


    )
    email = models.EmailField(blank=False)

    age = models.IntegerField(
        help_text="Age requirement: 21 years and above.",
        validators=[MinValueValidator(21)]
    )

    password = models.CharField(
        max_length=20,

    )
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=25
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=25
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )