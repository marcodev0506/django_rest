from rest_framework import serializers

from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer
from datetime import date


class PatientSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)# read_only es para que sea solo lectura
    age = serializers.SerializerMethodField() #Nos premite hacer calculos y retornar un valor 
    # Un serializador anidado nos permite  mostrar diferentes valores para una clave. Ya no es solamente clave valor, nos permite asi mostrar más información de un serializador

    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointments',

        ]
    def get_age(self, obj):
        age_td = date.today() - obj.date_of_birth
        years = age_td.days // 365
        return f"{years} años" #Al colocarlo en {} podemos retornar un string 

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'