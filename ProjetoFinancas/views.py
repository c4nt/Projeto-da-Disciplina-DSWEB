from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, '')

class cadastro_usuario(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro.html')
 
