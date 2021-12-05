from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="top"),
    path("topRedirect", views.topRedirect, name="topRedirect"),
    path("<int:number_id>", views.number, name="number"),
    path("form", views.form, name="form"),
    path("tweets", views.tweets, name="tweets"),
    path("search", views.search, name="search"),
    path("search2", views.search2, name="search2"),
    path("EditDelete", views.editDelete, name="EditDelete"),
    path("login", views.login, name="login"),
    path("api/user", views.apiuser, name="apiuser"),
]
