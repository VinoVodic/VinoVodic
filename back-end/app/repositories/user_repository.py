from django.contrib.auth.models import User

from app.models import Winery


class UserRepository:
    def get_user(self, username: str) -> User:
        return User.objects.get(username=username)

    def get_favorites(self, user: User) -> list[Winery]:
        return fav if (fav := user.extended.favorites) else []

    def add_favorite(self, user: User, winery: Winery) -> None:
        user.extended.favorites.add(winery)

    def delete_favorite(self, user: User, winery: Winery) -> None:
        user.extended.favorites.remove(winery)

    def get_visited(self, user: User) -> list[Winery]:
        return vis if (vis := user.extended.visited) else []

    def add_visited(self, user: User, winery: Winery) -> None:
        user.extended.visited.add(winery)

    def delete_visited(self, user: User, winery: Winery) -> None:
        user.extended.visited.remove(winery)
