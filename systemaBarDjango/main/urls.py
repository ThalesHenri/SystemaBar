from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('administradorLogin/', views.administradorLogin, name='administradorLogin'),
    path('cadastrarAdministradorEvent/', views.cadastrarAdministradorEvent, name='cadastrarAdministradorEvent'),
    path('cadastrarAdministrador/', views.cadastrarAdministrador, name='cadastrarAdministrador'),
    path('administradorDashboard/', views.administradorDashboard, name='administradorDashboard'),
    path('administradorDashboard/gerenciarAdministradores', views.gerenciarAdministradores, name='gerenciarAdministradores'),
    path('administradorDashboard/gerenciarAdministradores/editar/<int:pk>/', views.editarAdministrador, name='editarAdministrador'),
    path('administradorDashboard/gerenciarAdministradores/deletar/<int:admin_id>/', views.deletarAdministrador, name='deletarAdministrador'),
    path('administradorDashboard/gerenciarGarcom', views.gerenciarGarcom, name='gerenciarGarcom'),
    path('administradorDashboard/gerenciarGarcons/editar/<int:pk>/', views.editarGarcom, name='editarGarcom'),
    path('administradorDashboard/gerenciarGarcons/deletar/<int:garcom_id>/', views.deletarGarcom, name='deletarGarcom'),
    path('administradorDashboard/gerenciarCozinha', views.gerenciarCozinha, name='gerenciarCozinha'),
    path('administradorDashboard/gerenciarCozinha/editar/<int:pk>/', views.editarCozinha, name='editarCozinha'),
    path('administradorDashboard/gerenciarCozinha/deletar/<int:cozinha_id>/', views.deletarCozinha, name='deletarCozinha'),
    path('administradorDashboard/gerenciarCardapio', views.gerenciarCardapio, name='gerenciarCardapio'),
    path('administradorDashboard/gerenciarCardapio/adicionarItemCardapio/', views.adicionarItemCardapio, name='adicionarItemCardapio'),
    path('cozinhaLogin/', views.cozinhaLogin, name='cozinhaLogin'),
    path('cadastrarCozinhaEvent/', views.cadastrarCozinhaEvent, name='cadastrarCozinhaEvent'),
    path('cadastrarCozinha/', views.cadastrarCozinha, name='cadastrarCozinha'),
    path('cozinhaDashboard/', views.cozinhaDashboard, name='cozinhaDashboard'),
    path('escolhaCadastro/', views.escolhaCadastro, name='escolhaCadastro'),
    path('garcomLogin/', views.garcomLogin, name='garcomLogin'),
    path('cadastrarGarcomEvent/', views.cadastrarGarcomEvent, name='cadastrarGarcomEvent'),
    path('cadastrarGarcom/', views.cadastrarGarcom, name='cadastrarGarcom'),
    path('garcomDashboard/', views.garcomDashboard, name='garcomDashboard'),
    path('garcomDashboard/novoPedido', views.garcomNovoPedido, name='garcomNovoPedido'),
    path('garcomDashboard/novoPedidoEvent', views.garcomNovoPedidoEvent, name='garcomNovoPedidoEvent'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    


    
    
    
    
    

]
