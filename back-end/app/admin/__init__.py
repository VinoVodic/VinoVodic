from django.contrib import admin
from django.contrib.auth.models import User


from app.models import City, Review, Winery

from .city_admin import CityAdmin
from .review_admin import ReviewAdmin
from .winery_admin import WineryAdmin
from .extended_user_admin import ExtendedUserAdmin, UserAdmin  # noqa: F401

admin.site.register(City, CityAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Winery, WineryAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
