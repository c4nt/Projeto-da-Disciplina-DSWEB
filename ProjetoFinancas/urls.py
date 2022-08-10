from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('cadastro/', views.cadastro_usuario.as_view(), name='cadastro'),
    path('despesas/', views.listar_despesas.as_view(), name='listar_despesas'),
    path('balancete/', views.gerar_balancete.as_view(), name='gerar_balancete'),
    
]