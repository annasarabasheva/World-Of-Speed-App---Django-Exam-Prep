from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars.validators import year_validator
from profiles.models import Profile


class Car(models.Model):
    TYPE_CHOICES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    ]

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )
    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1)]
    )

    year = models.IntegerField(
        validators=[year_validator]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={
            "unique": "This image URL is already in use! Provide a new one."
        }

    )

    price = models.FloatField(
        validators=[MinValueValidator(1.0)]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='cars'
    )