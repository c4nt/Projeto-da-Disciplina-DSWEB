from django.contrib import admin
from .models import Entrada, Saida, Status, Usuario, Balancete

admin.site.register(Status)
admin.site.register(Usuario)
admin.site.register(Balancete)
admin.site.register(Entrada)
admin.site.register(Saida)




