from django.db import models


class City(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Град"
        verbose_name_plural = "Градови"
        db_table = "city"
