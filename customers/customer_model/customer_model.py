from django.db import models

from config.settings import base
from hopterlink.shared.utils import phone_number_validator


class Customer(models.Model):
    user = models.ForeignKey(base.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, validators=[phone_number_validator])
    invite_link = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
