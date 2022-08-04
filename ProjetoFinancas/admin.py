from django.contrib import admin
from .models import Despesas, Status, Usuario

admin.site.register(Status)
admin.site.register(Despesas)
admin.site.register(Usuario)


