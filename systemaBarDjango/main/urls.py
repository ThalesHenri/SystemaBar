from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('administradorLogin/', views.administradorLogin, name='administradorLogin'),
     path('cadastrarAdministradorEvent/', views.cadastrarAdministradorEvent, name='cadastrarAdministradorEvent'),
    path('cadastrarAdministrador/', views.cadastrarAdministrador, name='cadastrarAdministrador'),
    
    
    

]
