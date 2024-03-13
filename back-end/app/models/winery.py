from django.db import models

from .city import City
from .coords import Coords


class Winery(models.Model):
    name = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField()
    phone = models.TextField()
    work = models.TextField(blank=True, null=True)
    coords = models.ForeignKey(Coords, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def rating(self):
        temp = [r.rating for r in self.reviews.all()]
        return round(sum(temp) / len(temp), 1) if temp else 0

    def __str__(self) -> str:
        return f"{self.name} - {self.city}"

    class Meta:
        verbose_name = "Винарија"
        verbose_name_plural = "Винарии"
        db_table = "winery"
