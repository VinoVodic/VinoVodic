from django.db import models


class Coords(models.Model):
    longitude = models.TextField()
    latitude = models.TextField()

    def __str__(self) -> str:
        return f"{self.longitude} - {self.latitude}"

    class Meta:
        verbose_name = "Координати"
        verbose_name_plural = "Координати"
        db_table = "coords"
