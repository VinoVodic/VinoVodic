from typing import Any

from django.contrib.auth.models import User


class UserService:
    def get_user(self, username: str) -> User:
        raise NotImplementedError

    def update_user(self, username: str, data: dict[str, Any]) -> None:
        raise NotImplementedError

    def get_favorites(self, username: str) -> dict[str, Any]:
        raise NotImplementedError

    def add_favorite(self, username: str, data: dict[str, Any]) -> None:
        raise NotImplementedError

    def get_visited(self, username: str) -> dict[str, Any]:
        raise NotImplementedError

    def add_visited(self, username: str, data: dict[str, Any]) -> None:
        raise NotImplementedError
