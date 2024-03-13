from django.contrib.auth.models import User

from rest_framework import serializers
from .profile_review_serializer import ProfileReviewSerializer


class ProfileUserSerializer(serializers.ModelSerializer):
    reviews = ProfileReviewSerializer(required=True, many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "reviews",
        ]