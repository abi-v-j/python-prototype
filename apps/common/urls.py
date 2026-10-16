from django.urls import path
from . import views

app_name = "common"

urlpatterns = [
    path("checking/", views.checking, name="checking"),
    path("addtwonumbers/", views.add_two_numbers, name="add_two_numbers"),
    path("additem/", views.add_item, name="add_item"),
]