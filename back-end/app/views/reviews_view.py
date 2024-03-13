import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app.injector import injector
from app.services import UserService, ReviewService
from app.exceptions import InvalidInputError, UserHasNoPermission


class ReviewsView(APIView):
    # View can only be accessed if user is authenticated
    permission_classes = (IsAuthenticated,)
    # Necessary services
    user_service = injector.get(UserService)
    review_service = injector.get(ReviewService)

    def post(self, request, format=None) -> Response:
        """
        Add review for winery
        Parameters:
            winery_id: int
            rating: float
            comment: str | None
        """
        user = self.user_service.get_user(request.user)
        data = json.loads(request.body.decode("utf-8"))
        self.review_service.create_review(user, data)

        return Response(status=status.HTTP_201_CREATED)

    def put(self, request, format=None) -> Response:
        """
        Edit review
        Parameters:
            review_id: int
            winery_id: int
            rating: float
            comment: str
        """
        user = self.user_service.get_user(request.user)

        try:
            self.review_service.edit_review(user, request.data)
            return Response(status=status.HTTP_200_OK)
        except (InvalidInputError, UserHasNoPermission) as err:
            return Response(
                data={"data": str(err)}, status=status.HTTP_406_NOT_ACCEPTABLE
            )

    def delete(self, request, format=None) -> Response:
        """
        Delete review
        Parameters:
            review_id: int
        """
        self.review_service.delete_review(request.data)
        return Response(status=status.HTTP_200_OK)
