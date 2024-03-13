class CityNotFoundError(Exception):
    "Raise when city with given id is not in the database"

    def __init__(self, city_id) -> None:
        message = f"City with {city_id} not found."
        super().__init__(message)
