
from django.contrib import admin
from django.urls import path

from patients.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patients', list_patients),
    path('api/patients_create', create_patient)
]