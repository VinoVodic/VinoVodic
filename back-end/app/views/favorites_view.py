import json
from typing import Any

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.injector import injector
from app.services import UserService


class FavoritesView(APIView):
    # View can only be accessed if user is authenticated
    permission_classes = (IsAuthenticated,)
    # Necessary services
    user_service = injector.get(UserService)

    def get(self, request, format=None) -> Response:
        """
        Get favorite wineries.
        Parameters:
            N/A
        Returns:
            data: dict[str, Any]
        """
        data: dict[str, Any] = {}
        data["favorites"] = self.user_service.get_favorites(request.user)

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """
        Add winery to favorites.

        Parameters:
            winery_id: int
        Returns:
            status 200 OK
        """
        data = json.loads(request.body.decode("utf-8"))
        self.user_service.add_favorite(request.user, data)

        return Response(status=status.HTTP_202_ACCEPTED)

    def delete(self, request, format=None) -> Response:
        """
        Delete winery from favorites
        Parameters:
            winery_id: int
        """
        data = json.loads(request.body.decode("utf-8"))
        self.user_service.delete_favorite(request.user, data)

        return Response(status=status.HTTP_200_OK)

