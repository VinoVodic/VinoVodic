from app.models import City


class CityRepository:
    def get_city_by_id(self, city_id: int) -> City | None:
        if city := City.objects.get(pk=city_id):
            return city

    def get_all_cities(self) -> list[City] | None:
        if cities := City.objects.all().order_by("name"):
            return cities
