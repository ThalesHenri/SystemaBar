from django import forms
from django.forms import inlineformset_factory
from .models import AdminModel,CozinhaModel,GarcomModel,Pedido,ItemPedido, ItemCardapio

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
        fields = ['pagamento','mesa']
        

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['item_cardapio', 'quantidade']
        

ItemPedidoFormSet = inlineformset_factory(
    Pedido,
    ItemPedido,
    form=ItemPedidoForm,
    extra=1,  # Number of empty forms to display
    can_delete=True  # Allows items to be removed from the formset
)
        
        

class ItemCardapioForm(forms.ModelForm):
    class Meta:
        model = ItemCardapio
        fields = ['nome', 'foto', 'preco']