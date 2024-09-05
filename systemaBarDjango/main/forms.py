from django import forms
from .models import AdminModel

class AdminForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AdminModel
        fields = ['usuario', 'email', 'senha']



class AdminLoginForm(forms.Form):
    email = forms.EmailField(label="email")
    senha = forms.CharField(widget=forms.PasswordInput)