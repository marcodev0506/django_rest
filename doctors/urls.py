
# from django.urls import path

# from doctors.views import * 

# urlpatterns = [
#    # path('doctors/', list_doctors),
#    # path('doctors/<int:pk>/', detail_doctors),
#    path('doctors/', ListDoctorsView.as_view()),
#    path('doctors/<int:pk>/', DetailDoctors.as_view()),
# ]
from django.urls import path

from .views import (
    ListDoctorView,
    DetailDoctorView,
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
)

urlpatterns = [
    path('doctors/', ListDoctorView.as_view()),
    path('doctors/<int:pk>/', DetailDoctorView.as_view()),
    path('departments/', ListDepartmentView.as_view()),
    path('departments/<int:id>/', DetailDepartmentView.as_view()),
    path('doctoravailabilities/', ListDoctorAvailabilityView.as_view()),
    path('doctoravailabilities/<int:id>/', DetailDoctorAvailabilityView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),
]