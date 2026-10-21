from django.urls import path
from . import views

app_name = "common"

urlpatterns = [
    path("checking/", views.checking, name="checking"),
    path("addtwonumbers/", views.add_two_numbers, name="add_two_numbers"),
    path("items/", views.insert_item_orm, name="insert-item-orm"),
    path("items/<int:pk>/update/", views.update_item_orm, name="update-item-orm"),
    path("items/<int:pk>/delete/", views.delete_item_orm, name="delete-item-orm"),


]