from django.contrib import admin
from django.urls import path, include
from patients.views import PacienteViewSet
from doctors.views import DoctorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pacientes', PacienteViewSet, basename='Pacientes')
router.register('medicos',DoctorViewSet, basename='Médicos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
