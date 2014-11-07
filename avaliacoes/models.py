from django.db import models
from django.contrib.auth.models import AbstractUser

class Avaliacao(models.Model):
	nome = models.CharField(max_length=100)
	idade = models.IntegerField()
	peso = models.DecimalField(max_digits=10, decimal_places=3)
	altura = models.DecimalField(max_digits=10, decimal_places=3)
	resultado = models.DecimalField(max_digits=10, decimal_places=3)
	MASCULINO = 'M'
	FEMININO = 'F'
	SEXY = (
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
    )
	sexo = models.CharField(max_length=2, choices=SEXY, default=MASCULINO)

class Usuario(AbstractUser):
	telefone = models.CharField(max_length=100, blank=True, null=True)