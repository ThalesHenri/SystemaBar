from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('administradorDashboard/gerenciarCardapio/editar/<int:pk>/', views.editarItemCardapio, name='editarItemCardapio'),
    path('administradorDashboard/gerenciarCardapio/deletar/<int:pk>/', views.deletarItemCardapio, name='deletarItemCardapio'),
    path('administradorDashboard/administradorPedidos',views.administradorPedidos, name='administradorPedidos'),
    path('cozinhaLogin/', views.cozinhaLogin, name='cozinhaLogin'),
    path('cadastrarCozinhaEvent/', views.cadastrarCozinhaEvent, name='cadastrarCozinhaEvent'),
    path('cadastrarCozinha/', views.cadastrarCozinha, name='cadastrarCozinha'),
    path('cozinhaDashboard/', views.cozinhaDashboard, name='cozinhaDashboard'),
    path('cozinhaDashboard/avancarPedido/<int:pedido_id>', views.cozinhaAvancarPedido, name='cozinhaAvancarPedido'),
    path('escolhaCadastro/', views.escolhaCadastro, name='escolhaCadastro'),
    path('garcomLogin/', views.garcomLogin, name='garcomLogin'),
    path('cadastrarGarcomEvent/', views.cadastrarGarcomEvent, name='cadastrarGarcomEvent'),
    path('cadastrarGarcom/', views.cadastrarGarcom, name='cadastrarGarcom'),
    path('garcomDashboard/', views.garcomDashboard, name='garcomDashboard'),
    path('garcomCardapio/', views.garcomCardapio, name='garcomCardapio'),
    path('garcomDashboard/novoPedido', views.garcomNovoPedido, name='garcomNovoPedido'),
    path('garcomDashboard/novoPedidoEvent', views.garcomNovoPedidoEvent, name='garcomNovoPedidoEvent'),
    path('garcomDashboar/FinalizarPedido/<int:pedido_id>', views.garcomFinalizarPedido,name='garcomFinalizarPedido'),
    path('clean-pedidos/', views.clean_pedidos, name='clean_pedidos'),
    path('clean-actions/', views.clean_actions, name='clean_actions'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

    
    


    
    
    
    
    


