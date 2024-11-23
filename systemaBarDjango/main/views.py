from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from .forms import AdminForm, AdminLoginForm, CozinhaForm, CozinhaLoginForm, GarcomForm, GarcomLoginForm, PedidoForm, ItemPedidoFormSet, ItemCardapioForm
from .models import AdminModel, CozinhaModel, GarcomModel, Pedido, ItemPedido,ItemCardapio
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.

def home(request):
    return render(request, 'index.html')


def escolhaCadastro(request):
    return render(request, 'escolhaCadastro.html')


def cadastrarAdministrador(request):
    form = AdminForm()
    return render(request, 'cadastrarAdministrador.html', {'form': form})


def cadastrarAdministradorEvent(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Administrador cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados.')
    else:
        form = AdminForm()
    return render(request, 'cadastrarAdministrador.html', {'form': form})



def administradorLogin(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                admin = AdminModel.objects.get(email=email)
                if admin.check_password(senha):  # Use the custom check_password method
                    login(request, admin, backend='main.backends.EmailAuthBackend')  # Log the user in
                    request.session['is_admin'] = True
                    messages.success(request, 'Login realizado com sucesso!')
                    return redirect('administradorDashboard')
                else:
                    messages.error(request, 'Credenciais inválidas. Verifique sua senha.')
            except AdminModel.DoesNotExist:
                messages.error(request, 'Credenciais inválidas. Verifique seu e-mail.')
    else:
        form = AdminLoginForm()

    return render(request, 'adminLogin.html', {'form': form})


@login_required
def administradorDashboard(request):
    if not request.session.get('is_admin'):
        return HttpResponse('Conflito entre admin e garçom.')
        
    return render(request, 'administradorDashboard.html')


def cadastrarCozinha(request):
    form = CozinhaForm()
    return render(request, 'cadastrarCozinha.html', {'form': form})


def cadastrarCozinhaEvent(request):
    if request.method == 'POST':
        form = CozinhaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cozinha cadastrada com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados.')
    else:
        form = CozinhaForm()
    return render(request, 'cadastrarCozinha.html', {'form': form})


def cozinhaLogin(request):
    if request.method == 'POST':
        form = CozinhaLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                cozinha = CozinhaModel.objects.get(email=email)
                if check_password(senha, cozinha.senha):  # Verifica a senha criptografada
                    login(request, cozinha)
                    messages.success(request, 'Login realizado com sucesso!')
                    return redirect('cozinhaDashboard')
                else:
                    messages.error(request, 'Credenciais inválidas. Verifique sua senha.')
            except CozinhaModel.DoesNotExist:
                messages.error(request, 'Credenciais inválidas. Verifique seu e-mail.')
    else:
        form = CozinhaLoginForm()

    return render(request, 'cozinhaLogin.html', {'form': form})


@login_required
def cozinhaDashboard(request):
    return render(request, 'cozinhaDashboard.html')


def cadastrarGarcom(request):
    form = GarcomForm()
    return render(request, 'cadastrarGarcom.html', {'form': form})


def cadastrarGarcomEvent(request):
    if request.method == 'POST':
        form = GarcomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Garçom cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados.')
    else:
        form = GarcomForm()
    return render(request, 'cadastrarGarcom.html', {'form': form})


def garcomLogin(request):
    if request.method == 'POST':
        form = GarcomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            garcom = authenticate(request, username=email, password=senha)

            if garcom is not None:
                login(request, garcom)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('garcomDashboard')  # Certifique-se que está redirecionando corretamente
            else:
                messages.error(request, 'Credenciais inválidas. Verifique seu e-mail ou senha.')
    else:
        form = GarcomLoginForm()

    return render(request, 'garcomLogin.html', {'form': form})



@login_required
def garcomDashboard(request):
    return render(request, 'garcomDashboard.html')


@login_required
def garcomNovoPedido(request):
    if request.method == "POST":
        pedido_form = PedidoForm(request.POST)
        item_formset = ItemPedidoFormSet(request.POST)

        if pedido_form.is_valid() and item_formset.is_valid():
            # Save Pedido
            pedido = pedido_form.save(commit=False)
            pedido.garcom = request.user  # Assign the current Garçom user
            pedido.save()

            # Save ItemPedido items and link them to Pedido
            item_formset.instance = pedido
            item_formset.save()

            return redirect('garcomDashboard')  # Redirect to the dashboard or another page
    else:
        pedido_form = PedidoForm()
        item_formset = ItemPedidoFormSet()

    context = {
        'pedido_form': pedido_form,
        'item_formset': item_formset,
    }
    return render(request, 'novoPedido.html', context)


def garcomNovoPedidoEvent(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pedido cadastrado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados.')
    else:
        form = PedidoForm()
    return render(request, 'novoPedido.html', {'form': form})


def garcomLogout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('garcomLogin')


@login_required
def gerenciarAdministradores(request):
    admins = AdminModel.objects.all() 
    return render(request, "gerenciarAdministradores.html", {"admins": admins})


@login_required
def editarAdministrador(request, pk):
    admin = AdminModel.objects.get(id=pk)
    if request.method == "POST":
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            messages.success(request, "Administrador editado com sucesso.")
            return redirect("gerenciarAdministradores")
    else:
        form = AdminForm(instance=admin)
    return render(request, "editarAdministrador.html", {"form": form,"admin":admin})

@login_required
def deletarAdministrador(request, admin_id):
    admin = get_object_or_404(AdminModel, pk=admin_id)
    admin.delete()
    messages.success(request, "Administrador excluido com sucesso.")
    return redirect("gerenciarAdministradores")


@login_required
def gerenciarGarcom(request):
    garcom = GarcomModel.objects.all() 
    return render(request, "gerenciarGarcom.html", {"garcom": garcom})



@login_required
def editarGarcom(request, pk):
    garcom = GarcomModel.objects.get(id=pk)
    if request.method == "POST":
        form = GarcomForm(request.POST, instance=garcom)
        if form.is_valid():
            form.save()
            messages.success(request, "Garcom editado com sucesso.")
            return redirect("gerenciarGarcom")
    else:
        form = GarcomForm(instance=garcom)
    return render(request, "editarGarcom.html", {"form": form, "garcom":garcom})

@login_required
def deletarGarcom(request, garcom_id):
    garcom = get_object_or_404(GarcomModel, pk=garcom_id)
    garcom.delete()
    messages.success(request, "Garçom excluido com sucesso.")
    return redirect("gerenciarGarcom")



@login_required
def gerenciarCozinha(request):
    cozinha = CozinhaModel.objects.all() 
    return render(request, "gerenciarCozinha.html", {"cozinha": cozinha})



@login_required
def editarCozinha(request, pk):
    cozinha = CozinhaModel.objects.get(id=pk)
    if request.method == "POST":
        form = CozinhaForm(request.POST, instance=cozinha)
        if form.is_valid():
            form.save()
            messages.success(request, "Cozinha editado com sucesso.")
            return redirect("gerenciarCozinha")
    else:
        form = CozinhaForm(instance=cozinha)
    return render(request, "editarCozinha.html", {"form": form, "cozinha":cozinha})

@login_required
def deletarCozinha(request, cozinha_id):
    cozinha = get_object_or_404(CozinhaModel, pk=cozinha_id)
    cozinha.delete()
    messages.success(request, "Cozinha excluido com sucesso.")
    return redirect("gerenciarCozinha")


@login_required
def gerenciarCardapio(request):
    menu = ItemCardapio.objects.all()
    form = ItemCardapioForm()
    return render(request, "gerenciarCardapio.html", {"menu": menu,"form": form})


@login_required
def adicionarItemCardapio(request):
    if request.method == "POST":
        form = ItemCardapioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item adicionado com sucesso.")
            return redirect("gerenciarCardapio")
    else:
        form = ItemCardapioForm()
    return render(request, "gerenciarCardapio.html", {"form": form})