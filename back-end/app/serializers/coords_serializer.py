from rest_framework import serializers

from app.models import Coords


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            "longitude",
            "latitude",
        ]
