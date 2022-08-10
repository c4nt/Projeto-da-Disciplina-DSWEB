from django.contrib import admin
from .models import Receita, Despesa, Status, Usuario, Balancete

admin.site.register(Status)
admin.site.register(Usuario)
admin.site.register(Balancete)
admin.site.register(Receita)
admin.site.register(Despesa)




