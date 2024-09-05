from django.shortcuts import render, HttpResponse,redirect
from .forms import AdminForm,AdminLoginForm
from .models import AdminModel
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.


def home(response):
    return render(response,'index.html')


def cadastrarAdministrador(response):
    form = AdminForm()

    return render(response, 'cadastrarAdministrador.html', {'form': form})



def cadastrarAdministradorEvent(response):
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
        

def administradorLogin(response):
    if response.method == 'POST':
        form = AdminLoginForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            # Autenticando o administrador
            try:
                admin = AdminModel.objects.get(email=email, senha=senha)
                # Você pode personalizar aqui a lógica de autenticação ou login
                response.session['admin_logged_in'] = admin.id  # Armazenar o id do admin na sessão
                messages.success(response, 'Login realizado com sucesso!')
                print('admin_logado')
                return redirect('home')  # Redireciona para o painel do administrador
            except AdminModel.DoesNotExist:
                messages.error(response, 'Credenciais inválidas. Verifique seu e-mail ou senha.')
    else:
        form = AdminLoginForm()

    return render(response, 'adminLogin.html', {'form': form})