from typing import Any

from django.contrib.auth.models import User

from metaclasses import SingletonMeta

from app.services import ReviewService
from app.serializers import ReviewSerializer
from app.repositories import ReviewRepository
from app.exceptions import InvalidInputError, UserHasNoPermission


class ReviewServiceImpl(ReviewService, metaclass=SingletonMeta):
    review_repository = ReviewRepository()

    def create_review(self, user: User, data: dict[str, Any]) -> None:
        self.review_repository.create_review(
            user,
            data["winery_id"],
            data["rating"],
            data.get("comment", None),
        )

    def edit_review(self, user: User, data: dict[str, Any]) -> None:
        review = self.review_repository.get_review_by_id(data["review_id"])
        serializer = ReviewSerializer(review, data=data)

        if review.user != user:
            raise UserHasNoPermission(user.username, "ReviewService.edit_review()")

        if serializer.is_valid():
            serializer.save(user=user)
        else:
            raise InvalidInputError("ReviewService.edit_review()")

    def delete_review(self, data: dict[str, Any]) -> None:
        self.review_repository.delete_review(data["review_id"])