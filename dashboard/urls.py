from django.urls import path
from .views import dashboard
from . import views

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('pdf/', views.download_report, name='pdf_report'),
]