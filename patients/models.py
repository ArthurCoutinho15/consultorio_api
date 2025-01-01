from django.db import models

class Paciente(models.Model):
    
    SEXO = (
        ('M', 'MASCULINO'), 
        ('F','FEMININO'),
    )
    
    nome = models.CharField(max_length=255, blank=False)
    cpf = models.CharField(max_length=11, blank=False ,unique=True)
    data_nascimento = models.DateField(blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False, default='M')
    telefone = models.CharField(max_length=11, blank=False,unique=True)
    endereco = models.CharField(max_length=255, blank=False)
    historico_medico = models.TextField()
    arquivo_medico = models.FileField(default='-',blank=True, null=True)
    
    def __str__(self):
        return self.nome