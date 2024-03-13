from typing import Any

from metaclasses import SingletonMeta

from app.models import City
from app.services import CityService
from app.serializers import CitySerializer
from app.repositories import CityRepository
from app.exceptions import CityNotFoundError


class CityServiceImpl(CityService, metaclass=SingletonMeta):
    city_repository = CityRepository()

    def get_city_by_id(self, city_id: int) -> dict[str, City]:
        if city := self.city_repository.get_city_by_id(city_id):
            return {"city": CitySerializer(city).data}
        raise CityNotFoundError(city_id)

    def get_all_cities(self) -> dict[str, list[City]]:
        if cities := self.city_repository.get_all_cities():
            return {"data": CitySerializer(cities, many=True).data}
        return {"data": []}

    def get_cities(
        self, data: dict[str, Any]
    ) -> dict[str, City] | dict[str, list[City]]:
        """
        Return city by id if city_id is provided in request
        Else return all cities

        Parameters <dict[str, Any]>:
            city_id: int | None
        """
        if city_id := data.get("city_id", None):
            return self.get_city_by_id(city_id)
        else:
            return self.get_all_cities()
