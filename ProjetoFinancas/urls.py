from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('cadastro-usuario/', views.cadastro_usuario.as_view(), name='cadastro_usuario'),
    path('<int:usuario_id>/dashboard/cadastro-contas/', views.cadastro_contas.as_view(), name='cadastro_contas'),
    path('despesas/', views.listar_despesas.as_view(), name='listar_despesas'),
    path('login/', views.login.as_view(), name='login'),
    path('<int:usuario_id>/dashboard/', views.dashboard.as_view(), name='dashboard'),
]