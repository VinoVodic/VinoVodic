import json

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from app.tests.mockup import CityModelFactory


class CityTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        CityModelFactory.create_batch(5)

    def test_get_cities(self) -> None:
        url = reverse("app-cities")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

    def test_get_cities_with_city_id_parameter(self) -> None:
        url = reverse("app-cities")
        city_id = 1  # Must be smaller than batch_size
        response = self.client.get(f"{url}?city_id={city_id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

        city = json.loads(response.content)
        self.assertIn("city", city)
        
        city = city["city"]
        self.assertEqual(city["id"], city_id)
