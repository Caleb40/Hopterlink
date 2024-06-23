from django.db import models

from config.settings import base
from hopterlink.shared.utils import TimeStampMixin
from hopterlink.shared.utils import phone_number_validator


class Business(TimeStampMixin):
    """Fields for the Business Provider user"""

    class BusinessChoices(models.TextChoices):
        pass

    class IndustryChoices(models.TextChoices):
        pass

    # Owner Information
    owner = models.ForeignKey(base.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    logo = models.CharField(max_length=255, blank=True)

    # Business Information
    business_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=25, choices=IndustryChoices)
    location = models.CharField(max_length=255)
    business_type = models.CharField(max_length=25, choices=BusinessChoices)
    occupation = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    business_phone_1 = models.CharField(
        max_length=15,
        validators=[phone_number_validator],
    )
    business_phone_2 = models.CharField(
        max_length=15,
        blank=True,
        validators=[phone_number_validator],
    )

    # Delivery Information
    min_delivery_time_in_days = models.IntegerField()
    max_delivery_time_in_days = models.IntegerField()

    # Profile Information
    is_kyc_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    toc_accepted = models.BooleanField(default=False)
    business_reg_no = models.CharField(max_length=50, blank=True)
