from typing import Any

from django.contrib.auth.models import User

from metaclasses import SingletonMeta

from app.services import UserService
from app.serializers import WinerySerializer
from app.repositories import WineryRepository
from app.repositories import UserRepository
from app.exceptions import PasswordsDontMatchError


class UserServiceImpl(UserService, metaclass=SingletonMeta):
    user_repository = UserRepository()
    winery_repository = WineryRepository()

    def get_user(self, username: str) -> User:
        return self.user_repository.get_user(username)

    def update_user(self, username: str, data: dict[str, Any]) -> None:
        user = self.user_repository.get_user(username)

        if tmp := data.get("first_name", None):
            user.first_name = tmp
        if tmp := data.get("last_name", None):
            user.last_name = tmp
        if tmp := data.get("email", None):
            user.email = tmp
        if tmp := data.get("username", None):
            user.username = tmp
        if old_pw := data.get("old_password", None):
            if user.check_password(old_pw):
                new_pw = data.get("new_password", None)
                user.set_password(new_pw)
            else:
                raise PasswordsDontMatchError()

        user.save()

    def get_favorites(self, username: str) -> dict[str, Any]:
        user = self.user_repository.get_user(username)
        favorites = self.user_repository.get_favorites(user)

        return WinerySerializer(favorites, many=True).data

    def add_favorite(self, username: str, data: dict[str, Any]) -> None:
        user = self.user_repository.get_user(username)
        winery = self.winery_repository.get_winery_by_id(data["winery_id"])
        self.user_repository.add_favorite(user, winery)

    def delete_favorite(self, username: str, data: dict[str, Any]) -> None:
        user = self.user_repository.get_user(username)
        winery = self.winery_repository.get_winery_by_id(data["winery_id"])
        self.user_repository.delete_favorite(user, winery)

    def get_visited(self, username: str) -> dict[str, Any]:
        user = self.user_repository.get_user(username)
        visited = self.user_repository.get_visited(user)

        return WinerySerializer(visited, many=True).data

    def add_visited(self, username: str, data: dict[str, Any]) -> None:
        user = self.user_repository.get_user(username)
        winery = self.winery_repository.get_winery_by_id(data["winery_id"])
        self.user_repository.add_visited(user, winery)

    def delete_visited(self, username: str, data: dict[str, Any]) -> None:
        user = self.user_repository.get_user(username)
        winery = self.winery_repository.get_winery_by_id(data["winery_id"])
        self.user_repository.delete_visited(user, winery)
