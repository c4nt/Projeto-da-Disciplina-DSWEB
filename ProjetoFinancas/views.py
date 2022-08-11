from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Despesa, Receita, Balancete, Usuario
from django.contrib.auth.models import User
from django.urls import reverse


class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')

class cadastro_usuario(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro.html')
    def post(self, request, *args, **kwargs):
        nome = request.POST['nome']
        senha = request.POST['senha']
        if nome and senha:
            user = User.objects.create(username=nome, password=senha)
            Usuario.objects.create(user=user)
        return HttpResponseRedirect(reverse('index'))

class listar_despesas(View):
    def get(self, request, *args, **kwargs):
        despesas = Despesa.objects.all()
#        balancete = Balancete.objects.get(pk=1)
        context = {
            'despesas': despesas,
#           'balancete': balancete
        }
        return render(request, 'listar_despesas.html', context=context )

class login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


class gerar_balancete(View):
    def get(self, request, *args, **kwargs):
#        balancete = Balancete.objects.get(pk=balancete_id)
#        context = {
#           'balancete':balancete
#      }
        return render(request, 'gerar_balancete.html')
