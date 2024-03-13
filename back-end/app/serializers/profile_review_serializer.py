from rest_framework import serializers

from app.models import Review
from .profile_winery_serializer import ProfileWinerySerializer


class ProfileReviewSerializer(serializers.ModelSerializer):
    winery = ProfileWinerySerializer(required=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "rating",
            "comment",
            "winery",
        ]
