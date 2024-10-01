from django import forms
from .models import AdminModel, CozinhaModel

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