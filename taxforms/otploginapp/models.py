from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Associated User',
        related_name='client',
    )

    phone_number = models.CharField(
        blank=False,
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',  # Regex for exactly 10 digits
                message="Phone number must be exactly 10 digits."
            )
        ],
    )

    otp = models.CharField(
        blank=False,
        max_length=10,
    )



