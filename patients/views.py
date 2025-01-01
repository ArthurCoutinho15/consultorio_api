from django.shortcuts import render
from patients.models import Paciente
from patients.serializers import PacienteSerializer
from rest_framework import viewsets

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('id')
    serializer_class = PacienteSerializer

