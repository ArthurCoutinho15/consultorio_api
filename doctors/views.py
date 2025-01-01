from django.shortcuts import render
from doctors.serializers import DoctorSerializer
from doctors.models import Doctor
from rest_framework import viewsets


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
