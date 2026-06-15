from django.urls import path
from .views import *

urlpatterns = [
    path("", animal_list, name="animal_list"),
    path("add/", animal_create, name="animal_create"),
    path("update/<int:pk>/", animal_update, name="animal_update"),
    path("delete/<int:pk>/", animal_delete, name="animal_delete"),
]