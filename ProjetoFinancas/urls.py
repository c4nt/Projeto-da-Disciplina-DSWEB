from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('cadastro/', views.cadastro_usuario.as_view(), name='cadastro_usuario'),
    path('despesas/', views.listar_despesas.as_view(), name='listar_despesas'),
    path('login/', views.login.as_view(), name='login'),
    path('<int:balancete_id>/balancete/', views.gerar_balancete.as_view(), name='gerar_balancete'),
    
]