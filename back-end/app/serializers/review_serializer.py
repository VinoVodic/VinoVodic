from rest_framework import serializers

from app.models import Review
from app.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "rating",
            "comment",
        ]
