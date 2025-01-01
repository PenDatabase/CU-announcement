from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("official/", views.official, name="official"),
    path("search/<str:page>", views.search_announcements_view, name="announcements_search")
]
