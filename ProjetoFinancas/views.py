from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Despesa, Receita, Balancete, Usuario


class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')

class cadastro_usuario(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro.html')
 
class listar_despesas(View):
    def get(self, request, *args, **kwargs):
        despesas = Despesa.objects.all()
#        balancete = Balancete.objects.get(pk=1)
        context = {
            'despesas': despesas,
#           'balancete': balancete
        }
        return render(request, 'listar_despesas.html', context=context )

class gerar_balancete(View):
    def get(self, request, *args, **kwargs):
#        balancete = Balancete.objects.get(pk=balancete_id)
#        context = {
#           'balancete':balancete
#      }
        return render(request, 'gerar_balancete.html')
