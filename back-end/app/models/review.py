from django.db import models
from django.contrib.auth.models import User

from .winery import Winery


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="reviews"
    )
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    winery = models.ForeignKey(Winery, related_name="reviews", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"User: {self.user.username}, Winery:{str(self.winery)}"
