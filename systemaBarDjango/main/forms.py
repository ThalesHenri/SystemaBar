from django import forms
from .models import AdminModel,CozinhaModel,GarcomModel,Pedido

class AdminForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AdminModel
        fields = ['usuario', 'email', 'senha']

class AdminLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    senha = forms.CharField(widget=forms.PasswordInput)

class CozinhaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CozinhaModel
        fields = ['usuario', 'email', 'senha']


class CozinhaLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    senha = forms.CharField(widget=forms.PasswordInput)
    
    
class GarcomForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = GarcomModel
        fields = ['usuario', 'email', 'senha']

class GarcomLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    senha = forms.CharField(widget=forms.PasswordInput)
    
    
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['garcom','item_cardapio','quantidade','preco','pagamento','mesa']