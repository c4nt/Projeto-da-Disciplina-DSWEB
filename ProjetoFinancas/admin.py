from django.contrib import admin
from .models import Entrada, Saida, Despesas, Receitas, Status, Usuario, Balancete

admin.site.register(Status)
admin.site.register(Despesas)
admin.site.register(Usuario)
admin.site.register(Balancete)
admin.site.register(Receitas)
admin.site.register(Entrada)
admin.site.register(Saida)




