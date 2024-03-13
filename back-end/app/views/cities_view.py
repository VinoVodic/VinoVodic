from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app.injector import injector
from app.services import CityService
from app.exceptions import CityNotFoundError


class CitiesView(APIView):
    # Necessary services
    city_service = injector.get(CityService)

    def get(self, request, format=None) -> Response:
        """
        Returns cities by parameter. If no parameters are specified, returns all cities.

        Parameters:
            city_id: int | None
        Returns:
            dict[str, City] | dict[str, list[City]]
        """
        try:
            return Response(
                self.city_service.get_cities(request.GET), status=status.HTTP_200_OK
            )
        except CityNotFoundError as err:
            return Response(data={"data": str(err)}, status=status.HTTP_404_NOT_FOUND)
