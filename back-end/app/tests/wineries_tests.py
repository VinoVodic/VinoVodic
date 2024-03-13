import json

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from app.tests.mockup import CoordsModelFactory, CityModelFactory, WineryFactory


class WineryTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        coords_instance = CoordsModelFactory()
        city_instance = CityModelFactory()

        WineryFactory.create_batch(5, coords=coords_instance, city=city_instance)

    def test_get_wineries(self):
        url = reverse("app-wineries")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

    def test_get_wineries_with_winery_id_parameter(self):
        url = reverse("app-wineries")
        winery_id = 1  # Must be smaller than batch_size
        response = self.client.get(f"{url}?winery_id={winery_id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.accepted_media_type, "application/json")

        winery = json.loads(response.content)
        self.assertIn("winery", winery)

        winery = winery["winery"]
        self.assertEqual(winery["id"], winery_id)
