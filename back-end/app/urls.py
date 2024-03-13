from django.urls import path
from . import views

urlpatterns = [
    path("upsert", views.upsert_view, name="app-upsert"),
    path("cities", views.CitiesView.as_view(), name="app-cities"),
    path("wineries", views.WineriesView.as_view(), name="app-wineries"),

    path("favorites/", views.FavoritesView.as_view(), name="profiles-favorites"),
    path("visited/", views.VisitedView.as_view(), name="profiles-visited"),
    path("reviews/", views.ReviewsView.as_view(), name="profiles-reviews"),
    path("profile/", views.ProfileView.as_view(), name="profiles-profile"),
]
