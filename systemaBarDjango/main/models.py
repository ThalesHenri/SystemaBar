from django.db import models

# Create your models here.


class AdminModel(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
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
        return self.s
    
    
class Pedido(models.Model):
    garcom = models.ForeignKey('GarcomModel', on_delete=models.CASCADE)  # Trocar cliente por garçom
    item_cardapio = models.ForeignKey('ItemCardapio', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.BooleanField(default=False)  # Checkbox para pagamento
    data_pedido = models.DateTimeField(auto_now_add=True)
    mesa = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.garcom} - {self.item_cardapio} - Mesa: {self.mesa}'