from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    date_joined = models.DateField(
        default=timezone.now,
    )

