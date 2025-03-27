from django.db import models
from datetime import timedelta
from uuid import uuid4

from django.contrib.auth.models import User


class Flower(models.Model):
    count = models.IntegerField(default=0, blank=True)
    description = models.TextField(blank=True)
    delivered_at = models.DateTimeField(auto_now_add=True, blank=True,
                                        null=True)
    could_use_in_bouquet = models.BooleanField(default=True, null=True)
    wiki_page = models.URLField(
        default="https://www.wikipedia.org/",
        unique_for_date="delivered_at",
        null=True
    )
    name = models.CharField(max_length=64, unique=True, blank=True)


class Bouquet(models.Model):
    shop = models.Manager()
    fresh_period = models.DurationField(
        default=timedelta(days=5), null=True,
        help_text="Use this field if you need"
        " to have information about fresh time"
    )
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField(default=1.0, null=True)
    flowers = models.ManyToManyField(
        Flower,
        verbose_name="Flowers in bouquet"
    )


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    second_email = models.EmailField(null=True)
    name = models.CharField(max_length=64, null=True)
    invoice = models.FileField(null=True)
    user_uuid = models.UUIDField(editable=False, default=uuid4,
                                 null=True)
    discount_size = models.DecimalField(decimal_places=4, max_digits=6,
                                        null=True)
    client_ip = models.GenericIPAddressField(blank=True, null=True,
                                             protocol="IPv4")
