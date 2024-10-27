from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('administradorLogin/', views.administradorLogin, name='administradorLogin'),
    path('cadastrarAdministradorEvent/', views.cadastrarAdministradorEvent, name='cadastrarAdministradorEvent'),
    path('cadastrarAdministrador/', views.cadastrarAdministrador, name='cadastrarAdministrador'),
    path('administradorDashboard/', views.administradorDashboard, name='administradorDashboard'),
    path('cozinhaLogin/', views.cozinhaLogin, name='cozinhaLogin'),
    path('cadastrarCozinhaEvent/', views.cadastrarCozinhaEvent, name='cadastrarCozinhaEvent'),
    path('cadastrarCozinha/', views.cadastrarCozinha, name='cadastrarCozinha'),
    path('cozinhaDashboard/', views.cozinhaDashboard, name='cozinhaDashboard'),
    path('escolhaCadastro/', views.escolhaCadastro, name='escolhaCadastro'),
    path('garcomLogin/', views.garcomLogin, name='garcomLogin'),
    path('cadastrarGarcomEvent/', views.cadastrarGarcomEvent, name='cadastrarGarcomEvent'),
    path('cadastrarGarcom/', views.cadastrarGarcom, name='cadastrarGarcom'),
    path('garcomDashboard/', views.garcomDashboard, name='garcomDashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),


    
    
    
    
    

]
