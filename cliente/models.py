from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    def __str__(self):
        return self.nome

    telefone = models.CharField(max_length=15)
    def __str__(self):
        return self.telefone

    email = models.CharField(max_length=60)
    def __str__(self):
        return self.email

    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.senha

    def check_password(self, senha):
        return check_password(senha, self.senha)
