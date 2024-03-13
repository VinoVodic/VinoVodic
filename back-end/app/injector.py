from injector import Injector

from app.modules import CityModule, WineryModule, UserModule, ReviewModule


injector = Injector(
    [
        CityModule,
        WineryModule,
        UserModule,
        ReviewModule,
    ]
)
