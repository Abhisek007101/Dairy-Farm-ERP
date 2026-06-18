from django.urls import path
from .views import *

urlpatterns =  [path("",milk_list,name="milk_list"),
                path("add/",milk_create,name="milk_create"),
                path("update/<int:pk>/",milk_update,name="milk_update"),
                path("delete/<int:pk>/",milk_delete,name="milk_delete"),
                ]