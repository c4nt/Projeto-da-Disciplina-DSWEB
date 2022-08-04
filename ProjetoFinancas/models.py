from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    descricao = models.CharField(max_length=20)
    def __str__(self):
        return self.descricao

class Despesas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao

class receitas(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    def __str__(self):
        return self.descricao

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Nome: {self.user.username}"