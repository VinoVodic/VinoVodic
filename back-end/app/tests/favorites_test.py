import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from auth.serializers import RegisterSerializer
from app.tests.mockup import CoordsModelFactory, CityModelFactory, WineryFactory


class FavoritesTest(APITestCase):
    def setUp(self):
        # Setup Wineries
        coords_instance = CoordsModelFactory()
        city_instance = CityModelFactory()

        WineryFactory.create_batch(5, coords=coords_instance, city=city_instance)

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
        self.authorization_header = f"Bearer {self.token}"

    def test_add_favorites_endpoint(self):
        url = reverse("profiles-favorites")
        data = {"winery_id": "1"}

        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION=self.authorization_header
        )
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_get_favorites_endpoint(self):
        url = reverse("profiles-favorites")
        response = self.client.get(url, HTTP_AUTHORIZATION=self.authorization_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

        favorites = json.loads(response.content)
        self.assertIn("favorites", favorites)
