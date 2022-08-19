from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import login, logout
from .models import Despesa, Receita, Balancete, Usuario
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')

class cadastro_usuario(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro_usuario.html')
    def post(self, request, *args, **kwargs):
        nome = request.POST['nome']
        senha = request.POST['senha']
        if nome and senha:
            user = User.objects.create(username=nome, password=senha)
            Usuario.objects.create(user=user)
        return HttpResponseRedirect(reverse('index'))

class cadastro_contas(View):
    def get(self, request, usuario_id, **kwargs): 
        usuario = Usuario.objects.get(pk=usuario_id)
        context = {
            'usuario':usuario
        }       
        return render(request, 'cadastro_contas.html', context=context)
        
    def post(self, request, usuario_id, **kwargs):
        usuario = Usuario.objects.get(pk=usuario_id)
        if request.POST["tipo"] == 'receita':
            Receita.objects.create(titular_entrada=usuario, descricao=request.POST["descricao"], valor=request.POST["valor"])
        elif request.POST["tipo"] == 'despesa':
            Despesa.objects.create(titular_saida=usuario, descricao=request.POST["descricao"], valor=request.POST["valor"])
        return HttpResponseRedirect(reverse('index'))

class listar_despesas(View):
    def get(self, request, *args, **kwargs):
        despesas = Despesa.objects.all()
        receitas = Receita.objects.all()
        y = 0
        z = 0
        for x in despesas:
            y += x.valor 
        for x in receitas:
            z += x.valor 
        saldo = z - y

        context = {
            'despesas': despesas,
            'receitas': receitas,
            'y':y,
            'z':z,
            'saldo':saldo
        }
        return render(request, 'listar_despesas.html', context=context )

class login(View):
     def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'login.html', context = {'usuarios':usuarios})

#    def post(self, request, *args, **kwargs):
 #       nome = request.POST['nome']
  #      senha = request.POST['senha']
   #     if user is not None:
    #        login(request, user)
     #       if hasattr(request.user, 'cliente'):
      #          return HttpResponseRedirect(reverse('dashboardcliente'))
       #     else:
         #       return HttpResponseRedirect(reverse('fretes_index'))
        # else:
       #     erro = 'Email e senha inválidas!'

#            return render(request, 'login-cadastros/login.html', {'erro': erro})

class dashboard(View):
    def get(self, request, usuario_id, *args, **kwargs):
        return render(request, 'dashboard.html')
