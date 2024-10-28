
from django.urls import path

from doctors.views import * 

urlpatterns = [
   # path('doctors/', list_doctors),
   # path('doctors/<int:pk>/', detail_doctors),
   path('doctors/', ListDoctorsView.as_view()),
   path('doctors/<int:pk>/', DetailDoctors.as_view()),
]