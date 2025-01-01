from django.contrib import admin
from patients.models import Paciente

class Pacientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento', 'sexo', 'telefone', 'endereco')
    list_display_links = ('id', 'nome',)
    list_per_page = 20
    search_fields = ('nome', 'cpf')
    
admin.site.register(Paciente, Pacientes)
