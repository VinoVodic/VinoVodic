import json
from typing import Any

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.injector import injector
from app.services import UserService
from app.serializers import ProfileUserSerializer
from app.exceptions import PasswordsDontMatchError


class ProfileView(APIView):
    # View can only be accessed if user is authenticated
    permission_classes = (IsAuthenticated,)
    # Necessary services
    user_service = injector.get(UserService)
    # user_service = UserService()

    def get(self, request, format=None) -> Response:
        """
        Get user details
        Parameters:
            N/A
        """
        data: dict[str, Any] = {}

        user = self.user_service.get_user(request.user)
        data["user"] = ProfileUserSerializer(user).data

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """
        Add review for winery
        Parameters:
            winery_id: int
            rating: int
            comment: str | None
        """
        data = json.loads(request.body.decode("utf-8"))

        try:
            self.user_service.update_user(request.user, data)
        except PasswordsDontMatchError as err:
            return Response(
                data={"data": str(err)}, status=status.HTTP_406_NOT_ACCEPTABLE
            )

        return Response(status=status.HTTP_200_OK)
