from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('<int:usuario_id>/dashboard/', views.dashboard.as_view(), name='dashboard'),
    path('<int:user_id>/dashboard/cadastro-contas/', views.cadastro_contas.as_view(), name='cadastro_contas'),
    path('<int:user_id>/dashboard/gerar-balancete/', views.gerar_balancete.as_view(), name='gerar_balancete'),
    path('<int:user_id>/dashboard/arquivo-de-contas/', views.arquivo_de_contas.as_view(), name='arquivo_de_contas'),
    path('cadastro-usuario/', views.cadastro_usuario.as_view(), name='cadastro_usuario'),
    path('despesas/', views.listar_despesas.as_view(), name='listar_despesas'),
]