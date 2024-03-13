from django.db import models
from django.contrib.auth.models import User

from app.models import Winery


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extended")
    favorites = models.ManyToManyField(Winery, related_name="extended_favorites")
    visited = models.ManyToManyField(Winery, related_name="extended_visited")
