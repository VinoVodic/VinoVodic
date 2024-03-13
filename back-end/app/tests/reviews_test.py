import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from auth.serializers import RegisterSerializer
from app.tests.mockup import CoordsModelFactory, CityModelFactory, WineryFactory


class ReviewsTest(APITestCase):
    def setUp(self):
        # Setup Wineries
        coords_instance = CoordsModelFactory()
        city_instance = CityModelFactory()

        WineryFactory.create_batch(5, coords=coords_instance, city=city_instance)
        # ==================== #

        # Register a user
        serializer = RegisterSerializer(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "password": "testpassword",
                "password2": "testpassword",
                "first_name": "First name",
                "last_name": "Last name",
            }
        )

        if serializer.is_valid():
            self.user = serializer.save()
        else:
            raise ValueError("Invalid user data provided")

        # Generate a JWT token for the registered user
        self.token = AccessToken.for_user(self.user)
        self.auth_header = f"Bearer {self.token}"

    def test_add_review(self):
        url = reverse("profiles-reviews")

        response = self.client.post(
            url,
            data={
                "rating": 4,
                "winery_id": 1,
                "comment": "testing komentar",
            },
            HTTP_AUTHORIZATION=self.auth_header,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # TODO kreiraj review u setup namesto vaka
    def test_edit_review(self):
        self.test_add_review()

        url = reverse("profiles-reviews")

        response = self.client.put(
            url,
            data={
                "rating": 3,
                "winery_id": 1,
                "comment": "testing dr komentar",
                "review_id": 1,
            },
            HTTP_AUTHORIZATION=self.auth_header,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reviews(self):
        url = reverse("profiles-profile")
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

        reviews = json.loads(response.content)
        self.assertIn("user", reviews)
        
        reviews = reviews["user"]
        self.assertIn("reviews", reviews)
