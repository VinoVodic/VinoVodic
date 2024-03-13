import factory

from app.models import Winery, Coords, City


class CoordsModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Coords

    longitude = factory.Faker("longitude")
    latitude = factory.Faker("latitude")


class CityModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Faker("city")


class WineryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Winery

    name = factory.Faker("name")
    address = factory.Faker("address")
    phone = factory.Faker("phone_number")
    work = factory.Faker("name")
    coords = factory.SubFactory(CoordsModelFactory)
    city = factory.SubFactory(CityModelFactory)
