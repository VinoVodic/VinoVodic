from typing import Any

from django.http import Http404
from django.shortcuts import get_object_or_404

from ..models import City, Coords, Winery


def upsert(data: list[dict[str, Any]]) -> None:
    for row in data:
        try:
            city = get_object_or_404(City, name=row["mesto"])
        except Http404:
            city = City.objects.create(name=row["mesto"])

        city.save()

        try:
            coords = get_object_or_404(
                Coords, longitude=row["mesto"], latitude=row["coords"][1]
            )
        except Http404:
            coords = Coords.objects.create(
                longitude=row["coords"][0], latitude=row["coords"][1]
            )

        coords.save()

        try:
            winery = get_object_or_404(Winery, name=row["name"])
        except Http404:
            winery = Winery.objects.create(name=row["name"])

        winery.city = city
        winery.address = row["adresa"]
        winery.phone = row["tel_br"]
        winery.work = row["rab_vreme"]
        winery.coords = coords

        winery.save()
