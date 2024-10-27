from django.shortcuts import render, HttpResponse,redirect
from .forms import AdminForm,AdminLoginForm,CozinhaForm,CozinhaLoginForm,GarcomForm,GarcomLoginForm
from .models import AdminModel,CozinhaModel,GarcomModel
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.


def home(response):
    return render(response,'index.html')


def escolhaCadastro(response):
    return render(response,'escolhaCadastro.html')


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
                return redirect('administradorDashboard')  # Redireciona para o painel do administrador
            except AdminModel.DoesNotExist:
                messages.error(response, 'Credenciais inválidas. Verifique seu e-mail ou senha.')
    else:
        form = AdminLoginForm()

    return render(response, 'adminLogin.html', {'form': form})


def administradorDashboard(response):
    return render(response,'administradorDashboard.html')


def cadastrarCozinha(response):
    form = CozinhaForm()

    return render(response, 'cadastrarCozinha.html', {'form': form})



def cadastrarCozinhaEvent(response):
    if response.method == 'POST':
        form = CozinhaForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'Cozinha cadastrado com sucesso!')
            print('Mensagem de Sucesso Cadastrada')
            return redirect('home')  # Redirecionar para a página inicial ou de login
        else:
            messages.error(response, 'Erro no cadastro. Verifique os dados.')
            print("Mensagem de erro cadastrada")
    else:
        form = CozinhaForm()
    


def cozinhaLogin(response):
    if response.method == 'POST':
        form = CozinhaLoginForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            # Autenticando o Cozinha
            try:
                cozinha = CozinhaModel.objects.get(email=email, senha=senha)
                # Você pode personalizar aqui a lógica de autenticação ou login
                response.session['cozinha_logged_in'] = cozinha.id  # Armazenar o id do cozinha na sessão
                messages.success(response, 'Login realizado com sucesso!')
                print('cozinha_logado')
                return redirect('cozinhaDashboard')  # Redireciona para o painel do administrador
            except CozinhaModel.DoesNotExist:
                messages.error(response, 'Credenciais inválidas. Verifique seu e-mail ou senha.')
    else:
        form = CozinhaLoginForm()

    return render(response, 'cozinhaLogin.html', {'form': form})


def cozinhaDashboard(response):
    return render(response,'cozinhaDashboard.html')


def cadastrarGarcom(response):
    form = GarcomForm()

    return render(response, 'cadastrarGarcom.html', {'form': form})



def cadastrarGarcomEvent(response):
    if response.method == 'POST':
        form = GarcomForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'Garcom cadastrado com sucesso!')
            print('Mensagem de Sucesso Cadastrada')
            return redirect('home')  # Redirecionar para a página inicial ou de login
        else:
            messages.error(response, 'Erro no cadastro. Verifique os dados.')
            print("Mensagem de erro cadastrada")
    else:
        form = GarcomForm()
    
        

def garcomLogin(response):
    if response.method == 'POST':
        form = GarcomLoginForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            
            # Autenticando o garcom
            try:
                garcom = GarcomModel.objects.get(email=email, senha=senha)
                # Você pode personalizar aqui a lógica de autenticação ou login
                response.session['garcom_logged_in'] = garcom.id  # Armazenar o id do garcom na sessão
                messages.success(response, 'Login realizado com sucesso!')
                print('garcom_logado')
                return redirect('garcomDashboard')  # Redireciona para o painel do administrador
            except GarcomModel.DoesNotExist:
                messages.error(response, 'Credenciais inválidas. Verifique seu e-mail ou senha.')
    else:
        form = GarcomLoginForm()

    return render(response, 'garcomLogin.html', {'form': form})


def garcomDashboard(response):
    return render(response,'garcomDashboard.html')
