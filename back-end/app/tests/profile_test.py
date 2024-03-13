import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from auth.serializers import RegisterSerializer


class ProfileTest(APITestCase):
    def setUp(self):
        # Register a user
        serializer = RegisterSerializer(
            data={
                "username": "testuser",
                "email": "test@example.com",
                "password": "testpassword",
                "password2": "testpassword",
                "first_name": "First name",
                "last_name": "Last name",
            },
        )

        if serializer.is_valid():
            self.user = serializer.save()
        else:
            raise ValueError("Invalid user data provided")

        # Generate a JWT token for the registered user
        self.token = AccessToken.for_user(self.user)
        self.auth_header = f"Bearer {self.token}"

    def test_get_user(self):
        url = reverse("profiles-profile")
        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

        resp_user = json.loads(response.content)
        self.assertIn("user", resp_user)
        
        resp_user = resp_user["user"]
        self.assertEqual(resp_user["id"], getattr(self.user, "id"))
        self.assertEqual(resp_user["username"], getattr(self.user, "username"))
        self.assertEqual(resp_user["first_name"], getattr(self.user, "first_name"))
        self.assertEqual(resp_user["last_name"], getattr(self.user, "last_name"))
        self.assertEqual(resp_user["last_name"], getattr(self.user, "last_name"))
        self.assertEqual(resp_user["email"], getattr(self.user, "email"))

    def test_update_user(self):
        url = reverse("profiles-profile")

        new_user_data = {
                "email": "newtesadasdt@example.com",
                "first_name": "New First name",
                "last_name": "New Last name",
            }

        response = self.client.post(
            url,
            data=new_user_data,
            HTTP_AUTHORIZATION=self.auth_header,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

        response = self.client.get(url, HTTP_AUTHORIZATION=self.auth_header)
        resp_user = json.loads(response.content)
        self.assertIn("user", resp_user)

        resp_user = resp_user["user"]
        self.assertEqual(resp_user["id"], getattr(self.user, "id"))
        self.assertEqual(resp_user["first_name"], new_user_data["first_name"])
        self.assertEqual(resp_user["last_name"], new_user_data["last_name"])
        self.assertEqual(resp_user["email"], new_user_data["email"])
