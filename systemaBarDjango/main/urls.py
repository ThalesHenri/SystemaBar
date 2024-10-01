from django.urls import path
from . import views

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
    
    
    

]
