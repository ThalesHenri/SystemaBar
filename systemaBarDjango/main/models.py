from django.db import models

# Create your models here.


class AdminModel(models.Model):
    usuario = models.CharField(max_length=100)
    bemail = models.EmailField(unique=True)
    senha  = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.usuario
    
    
class CozinhaModel(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha  = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.usuario
    

class GarcomModel(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha  = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.usuario


class ItemCardapio(models.Model):
    nome = models.CharField(max_length=100)
    preço = models.IntegerField()
    foto = models.ImageField(upload_to='fotos_cardapio/', blank=True,null=True)
    
    
    def __str__(self):
        return self.nome