
from django.contrib import admin
from django.urls import path , include

from patients.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docs.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('patients.urls')),
    path('api/', include('doctors.urls')),
    path('api/', include('bookings.urls')),
   
]