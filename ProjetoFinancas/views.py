from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import login, logout
from .models import Conta, Usuario
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from datetime import datetime



class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')

class cadastro_usuario(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro_usuario.html')
    def post(self, request, *args, **kwargs):
        user = User.objects.create(username=request.POST['nome'], password=request.POST['senha'])
        Usuario.objects.create(user=user, telefone=request.POST['telefone'], email=request.POST['email'])
        return HttpResponseRedirect(reverse('login'))

class cadastro_contas(View):
    def get(self, request, usuario_id, **kwargs): 
        usuario = Usuario.objects.get(pk=usuario_id)
        context = {
            'usuario':usuario
        }       
        return render(request, 'cadastro_contas.html', context=context)
        
    def post(self, request, usuario_id, **kwargs):
        usuario = Usuario.objects.get(pk=usuario_id)
        id = usuario.id
        if request.POST["tipo"] == 'receita':
            Conta.objects.create(titular=usuario, descricao=request.POST["descricao"], valor=request.POST["valor"], data_criacao=request.POST["data"], ehReceita=True)
        elif request.POST["tipo"] == 'despesa':
            Conta.objects.create(titular=usuario, descricao=request.POST["descricao"], valor=request.POST["valor"], data_criacao=request.POST["data"], ehDespesa=True)
        return HttpResponseRedirect(reverse('dashboard', args=(usuario.id,)))

class listar_despesas(View):
    def get(self, request, *args, **kwargs):
        contas = Conta.objects.all().order_by('data_criacao')
        y = 0
        z = 0
        for x in contas:
            if x.ehDespesa == True:
                y += x.valor 
            else:
                z += x.valor 
        saldo = z - y

        context = {
            'contas': contas,
            'y':y,
            'z':z,
            'saldo':saldo
        }
        return render(request, 'listar_despesas.html', context=context )

class gerar_balancete(View):
    def get(self, request, usuario_id, *args, **kwargs):
        usuario = Usuario.objects.get(pk=usuario_id)
        contas = Conta.objects.filter(titular__id = usuario_id, 
        data_criacao__month=datetime.today().month).order_by('data_criacao')
        y = 0
        z = 0
        for x in contas:
            if x.ehDespesa == True:
                y += x.valor
            else:
                z+= x.valor 
        saldo = z - y
        context = {
            'contas': contas,
            'y':y,
            'z':z,
            'saldo':saldo
        }
        return render(request, 'gerar_balancete.html', context=context )

class arquivo_de_contas(View):
    def get(self, request, usuario_id, **kwargs):
        usuario = Usuario.objects.get(pk=usuario_id)
        context = {
            'usuario':usuario
        }
        return render(request, 'arquivo_de_contas.html', context=context)

    def post(self, request, usuario_id, **kwargs):
        usuario = Usuario.objects.get(pk=usuario_id)
        m = request.POST['mes']
        if m == '':
            m = 0
        contas_mes = Conta.objects.filter(titular__id=usuario_id, data_criacao__month=m)
        msg = "Não exitem contas cadastradas neste período."
        y = 0
        z = 0
        for x in contas_mes:
            if x.ehDespesa == True:
                y += x.valor
            else:
                z+= x.valor 
        saldo = z - y
        context = {
            'contas_mes':contas_mes,
            'usuario':usuario,
            'y':y,
            'z':z,
            'saldo':saldo,
            'msg':msg
        }
        return render(request, 'arquivo_de_contas.html', context=context)

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
