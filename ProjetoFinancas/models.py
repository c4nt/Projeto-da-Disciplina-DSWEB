from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    descricao = models.CharField(max_length=20)
    def __str__(self):
        return self.descricao


class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telefone = models.IntegerField()
    email = models.EmailField(max_length=250)
    def __str__(self):
        return self.user.username

class Conta(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField()
    ehDespesa = models.BooleanField(default=False)
    ehReceita = models.BooleanField(default=False)
    def __str__(self):
        return self.descricao

class Balancete(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mes_ref = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.titular} - {self.mes_ref}"