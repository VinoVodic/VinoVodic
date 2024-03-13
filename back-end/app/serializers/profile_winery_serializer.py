from rest_framework import serializers
from app.models import Winery


class ProfileWinerySerializer(serializers.ModelSerializer):
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
        ]
