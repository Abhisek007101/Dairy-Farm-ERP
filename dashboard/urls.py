from django.urls import path
from .views import dashboard
from . import views

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path('dashboard/pdf/', views.download_report, name='pdf_report'),
]