from typing import Any


from django.contrib.auth.models import User


class ReviewService:
    def create_review(self, user: User, data: dict[str, Any]) -> None:
        raise NotImplementedError

    def edit_review(self, user: User, data: dict[str, Any]) -> None:
        raise NotImplementedError

    def delete_review(self, data: dict[str, Any]) -> None:
        raise NotImplementedError
