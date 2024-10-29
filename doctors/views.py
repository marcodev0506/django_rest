#----------------Vistas basadas en funciones ----------------
# @api_view(['GET', 'POST'])
# def list_doctors(request):
#     if request.method == 'GET':
#         patients = Doctor.objects.all()
#         serializer = DoctorSerializer(patients, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = DoctorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_doctors(request, pk):
#     try:
#         patient = Doctor.objects.get(id=pk)
#     except Doctor.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DoctorSerializer(patient)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = DoctorSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True) # exception para validar que se reciban los datos segun las reglas del serializador
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     if request.method == 'DELETE':
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#--------------------------Pasamos como parametro vistas genericas
# class ListDoctorsView(ListAPIView, CreateAPIView ):
#     allowed_methods =['GET', 'POST']
#     serializer_class= DoctorSerializer
#     queryset=Doctor.objects.all()

# ----------Usamos las vistas y definimos y tenemos mas control de los metodos 
# class DetailDoctors(APIView):
#     allowed_methods =['GET', 'PUT', 'DELETE']
#     def get (self,request,pk):
#         try:
#             patient = Doctor.objects.get(id=pk)
#         except Doctor.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         if request.method == 'GET':
#             serializer = DoctorSerializer(patient)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         try:
#             patient = Doctor.objects.get(id=pk)
#         except Doctor.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = DoctorSerializer(patient, data=request.data)
#         serializer.is_valid(raise_exception=True) # exception para validar que se reciban los datos segun las reglas del serializador
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     def delete(self,request,pk):
#         try:
#             patient = Doctor.objects.get(id=pk)
#         except Doctor.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class DetailDoctors(RetrieveUpdateDestroyAPIView):
#     allowed_methods =['GET', 'PUT', 'DELETE']
#     serializer_class= DoctorSerializer
#     queryset=Doctor.objects.all()

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Doctor,
    Department,
    DoctorAvailability,
    MedicalNote,
)
from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)


class ListDoctorView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()