
from django.urls import path

from patients.views import * 

urlpatterns = [
    path('patients/', list_patients),
    path('patients/<int:pk>/', detail_patient),
]