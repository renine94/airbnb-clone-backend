import uuid

from django.conf import settings
from django.db import models

from src.apps.accounts.models import User


class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.IntegerField()
    bedrooms = models.SmallIntegerField()
    bathrooms = models.SmallIntegerField()
    guests = models.SmallIntegerField()
    country = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    category = models.CharField(max_length=255)

    image = models.ImageField(upload_to="uploads/properties")
    landlord = models.ForeignKey(User, related_name="properties", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_url(self):
        return f"{settings.WEBSITE_URL}{self.image.url}"
