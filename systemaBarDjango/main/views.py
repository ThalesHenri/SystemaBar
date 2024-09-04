from django.shortcuts import render, HttpResponse,redirect
from .forms import AdminForm
from django.contrib import messages

# Create your views here.


def home(response):
    return render(response,'index.html')

def administradorLogin(response):
    return render(response,'administradorLogin.html')


def cadastrarAdministrador(response):
    form = AdminForm()

    return render(response, 'cadastrarAdministrador.html', {'form': form})



def administradorLoginEvent(response):
    if response.method == 'POST':
        form = AdminForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'Administrador cadastrado com sucesso!')
            print('Mensagem de Sucesso Cadastrada')
            return redirect('home')  # Redirecionar para a página inicial ou de login
        else:
            messages.error(response, 'Erro no cadastro. Verifique os dados.')
            print("Mensagem de erro cadastrada")
    else:
        form = AdminForm()