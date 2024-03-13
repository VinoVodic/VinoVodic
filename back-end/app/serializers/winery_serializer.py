from rest_framework import serializers

from app.models import Winery
from .city_serializer import CitySerializer
from .coords_serializer import CoordsSerializer
from .review_serializer import ReviewSerializer


class WinerySerializer(serializers.ModelSerializer):
    city = CitySerializer(required=True)
    coords = CoordsSerializer(required=True)
    reviews = ReviewSerializer(required=True, many=True)

    class Meta:
        model = Winery
        fields = [
            "id",
            "name",
            "city",
            "address",
            "phone",
            "work",
            "coords",
            "rating",
            "reviews",
        ]
