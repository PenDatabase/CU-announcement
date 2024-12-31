from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("official/", views.official, name="official"),
    path("official/search/", views.official_search, name="official_page_search")
]
