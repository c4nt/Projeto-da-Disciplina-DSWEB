from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    descricao = models.CharField(max_length=20)
    def __str__(self):
        return self.descricao


class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Nome: {self.user.username}"

class Balancete(models.Model):
    titular_balancete = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)

class Receita(models.Model):
    titular_entrada = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)
    balancete_ref = models.ForeignKey(Balancete, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    titular_saida = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateField(auto_now_add=True)
    balancete_ref = models.ForeignKey(Balancete, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.descricao

