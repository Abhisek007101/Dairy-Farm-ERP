from django.urls import path
from .views import *

urlpatterns = [

    path(
        "",
        sale_list,
        name="sale_list"
    ),

    path(
        "add/",
        sale_create,
        name="sale_create"
    ),

    path(
        "update/<int:pk>/",
        sale_update,
        name="sale_update"
    ),

    path(
        "delete/<int:pk>/",
        sale_delete,
        name="sale_delete"
    ),

]