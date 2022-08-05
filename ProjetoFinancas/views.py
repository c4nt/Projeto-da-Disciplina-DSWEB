from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Despesas, Balancete


class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing.html')

class cadastro_usuario(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro.html')
 
class listar_despesas(View):
    def get(self, request, *args, **kwargs):
        despesas = Despesas.objects.all()
        balancete = Balancete.objects.get(pk=1)
        context = {
            'despesas': despesas,
            'balancete': balancete
        }
        return render(request, 'listar_despesas.html', context=context )

#class balancete(View):
#    def get(self, request, *args, **kwargs):
