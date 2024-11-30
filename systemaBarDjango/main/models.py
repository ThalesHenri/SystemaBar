from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

# Create your models here.

class AdminModel(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)
    backend = 'main.backends,EmailAuthBackend'
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Verifica se é um novo registro
            self.senha = make_password(self.senha)  # Criptografa a senha
        if kwargs.pop('update_last_login', False):
            self.last_login = timezone.now()
        super().save(*args, **kwargs)
        
    
    def check_password(self, senha_plaintext):
        return check_password(senha_plaintext, self.senha)

    def __str__(self):
        return self.usuario
    
    @property
    def is_authenticated(self):
        # Retorne sempre True se o garçom estiver autorizado
        return True



class CozinhaModel(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    

    def save(self, *args, **kwargs):
        if not self.pk:  # Verifica se é um novo registro
            self.senha = make_password(self.senha)  # Criptografa a senha
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.usuario




class GarcomModel(models.Model):
    usuario = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Hashes the password only if it's newly set or modified
        if not self.pk or not check_password(self.senha, self.senha):
            self.senha = make_password(self.senha)

        # Updates last_login if `update_last_login` is set
        if kwargs.pop('update_last_login', False):
            self.last_login = timezone.now()

        super().save(*args, **kwargs)
    
    def check_password(self, senha_plaintext):
        return check_password(senha_plaintext, self.senha)

    def __str__(self):
        return self.usuario
    
    @property
    def is_authenticated(self):
        # Retorne sempre True se o garçom estiver autorizado
        return True


class ItemCardapio(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Alterado de IntegerField para DecimalField
    foto = models.ImageField(upload_to='fotos_cardapio/', blank=True, null=True)

    def __str__(self):
        return self.nome  # Corrigido o retorno para exibir o nome do item corretamente


class ItemPedido(models.Model):
    pedido =  models.ForeignKey('Pedido', on_delete=models.CASCADE, related_name='itens')
    item_cardapio = models.ForeignKey('ItemCardapio',on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    
    
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('criado', 'Criado'),
        ('preparando', 'Preparando'),
        ('pronto', 'Pronto')
    ]
    garcom = models.ForeignKey('GarcomModel', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.BooleanField(default=False)
    data_pedido = models.DateTimeField(auto_now_add=True)
    mesa = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='criado')

    def __str__(self):
        
        return f'{self.garcom} - {self.item_cardapio} - Mesa: {self.mesa}'


class RecentAction(models.Model):
    descricao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)