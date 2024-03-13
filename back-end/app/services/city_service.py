from typing import Any

from app.models import City


class CityService:
    def get_city_by_id(self, city_id: int) -> dict[str, City]:
        raise NotImplementedError

    def get_all_cities(self) -> dict[str, list[City]]:
        raise NotImplementedError

    def get_cities(
        self, data: dict[str, Any]
    ) -> dict[str, City] | dict[str, list[City]]:
        """
        Return city by id if city_id is provided in request
        Else return all cities

        Parameters <dict[str, Any]>:
            city_id: int | None
        """
        raise NotImplementedError
