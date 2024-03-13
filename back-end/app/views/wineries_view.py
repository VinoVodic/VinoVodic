from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app.injector import injector
from app.services import WineryService
from app.exceptions import WineryNotFoundError


class WineriesView(APIView):
    # Necessary services
    winery_service = injector.get(WineryService)

    def get(self, request, format=None) -> Response:
        """
        Returns wineries by parameter. Only one parameter can be active at a time.
        If no parameters are specified, returns all wineries.

        Parameters:
            winery_id: int | None
            city_id: int | None
        Returns:
            dict[str, Winery] | dict[str, list[Winery]]
        """
        try:
            return Response(
                self.winery_service.get_wineries(request.GET), status=status.HTTP_200_OK
            )
        except WineryNotFoundError as err:
            return Response(data={"data": str(err)}, status=status.HTTP_404_NOT_FOUND)
