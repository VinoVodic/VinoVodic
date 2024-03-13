from injector import Module, Binder, singleton

from app.services import CityService, WineryService, UserService, ReviewService
from app.services.implementations import CityServiceImpl, WineryServiceImpl, UserServiceImpl, ReviewServiceImpl


class CityModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(CityService, to=CityServiceImpl, scope=singleton)


class WineryModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(WineryService, to=WineryServiceImpl, scope=singleton)


class UserModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(UserService, to=UserServiceImpl, scope=singleton)


class ReviewModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(ReviewService, to=ReviewServiceImpl, scope=singleton)

