from django.db import models
from django.contrib.auth.models import AbstractUser

class Avaliacao(models.Model):
	nome = models.CharField(max_length=100)
	sexo = models.CharField(max_length=20)
	idade = models.IntegerField()
	peso = models.DecimalField(max_digits=10, decimal_places=3)
	altura = models.DecimalField(max_digits=10, decimal_places=3)
	resultado = models.DecimalField(max_digits=10, decimal_places=3)

class Usuario(AbstractUser):
	endereco = models.CharField(max_length=100, blank=True, null=True)