from django.db import models

class Doctor(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    crm = models.CharField(max_length=20, blank=False, unique=True)
    especialidade = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.nome