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


class Entrada(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.descricao

class Saida(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.descricao

class Despesas(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
#    def __str__(self):
#        return self.titular

class Receitas(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
#    def __str__(self):
#        return self.titular

class Balancete(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    receita = models.ForeignKey(Receitas, on_delete=models.CASCADE)
    despesas = models.ForeignKey(Despesas, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
