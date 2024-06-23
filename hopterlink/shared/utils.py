from django.core import validators
from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


phone_number_validator: validators.RegexValidator = validators.RegexValidator(
    regex=r"[+]?\d{11,14}",
    message="Invalid phone number",
)
