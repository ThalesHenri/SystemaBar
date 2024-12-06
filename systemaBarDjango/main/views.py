from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from .forms import AdminForm, AdminLoginForm, CozinhaForm, CozinhaLoginForm, GarcomForm, GarcomLoginForm, PedidoForm, ItemPedidoFormSet, ItemCardapioForm
from .models import AdminModel, CozinhaModel, GarcomModel, Pedido, ItemPedido,ItemCardapio, RecentAction
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
            action = RecentAction(descricao=f'Administrador {request.user} cadastrado com sucesso!')
            action.save()
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
                    action = RecentAction(descricao=f'Administrador {request.user} logado com sucesso!')
                    action.save()
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
    
    administradores = AdminModel.objects.all()
    garcons = GarcomModel.objects.all()
    cardapio = ItemCardapio.objects.all()
    context = {
    'recent_actions' : RecentAction.objects.all(),
    'administradores': administradores,
        'garcons': garcons,
        'cardapio': cardapio,
    
    }
    
        
    return render(request, 'administradorDashboard.html', context)


def cadastrarCozinha(request):
    form = CozinhaForm()
    return render(request, 'cadastrarCozinha.html', {'form': form})


def cadastrarCozinhaEvent(request):
    if request.method == 'POST':
        form = CozinhaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cozinha cadastrada com sucesso!')
            action = RecentAction(descricao=f'Cozinha {request.user} cadastrada com sucesso!')
            action.save()
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
                    login(request, cozinha,backend='main.backends.EmailAuthBackend')
                    messages.success(request, 'Login realizado com sucesso!')
                    action = RecentAction(descricao=f'Cozinha {request.user} logada com sucesso!') 
                    action.save()
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
    pedidos = Pedido.objects.all()
    context = {
        'pedidos':pedidos
    }
    return render(request, 'cozinhaDashboard.html',context=context)


def cadastrarGarcom(request):
    form = GarcomForm()
    return render(request, 'cadastrarGarcom.html', {'form': form})


def cadastrarGarcomEvent(request):
    if request.method == 'POST':
        form = GarcomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Garçom cadastrado com sucesso!')
            action = RecentAction(descricao=f'Garçom {request.user} cadastrado com sucesso!')  
            action.save()
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
                action = RecentAction(descricao=f'Garçom {request.user} logado com sucesso!')
                action.save()
                return redirect('garcomDashboard')  # Certifique-se que está redirecionando corretamente
            else:
                messages.error(request, 'Credenciais inválidas. Verifique seu e-mail ou senha.')
    else:
        form = GarcomLoginForm()

    return render(request, 'garcomLogin.html', {'form': form})



@login_required
def garcomDashboard(request):
    mesas_ocupadas_count = Pedido.objects.exclude(mesa__exact='').values('mesa').distinct().count()
    pedidos = Pedido.objects.filter(garcom=request.user).order_by('-id')
    pedidosProntos = Pedido.objects.filter(status='finalizado').count()
    context = {
        'mesas_ocupadas_count' : mesas_ocupadas_count,
        'pedidos':pedidos,
        'pedidosProntos' : pedidosProntos
    }
    # os itens não estão sendo adicionados aos pedidos.
    return render(request, 'garcomDashboard.html', context=context)


@login_required
def garcomCardapio(request):
    menu = ItemCardapio.objects.all()
    context = {
        'menu':menu
    }
    return render(request,'garcomCardapio.html',context=context)



@login_required
def garcomFinalizarPedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.status = 'finalizado'
    pedido.save()
    messages.success(request, 'Pedido finalizado com sucesso!')
    action = RecentAction(descricao=f'Garçom {request.user} finalizou um pedido!')
    action.save()
    return redirect('garcomDashboard')

@login_required
def garcomNovoPedido(request):
    if request.method == "POST":
        pedido_form = PedidoForm(request.POST)
        item_formset = ItemPedidoFormSet(request.POST)

        if pedido_form.is_valid() and item_formset.is_valid():
            pedido = pedido_form.save(commit=False)
            pedido.garcom = request.user
            pedido.save()

            item_formset.instance = pedido
            item_formset.save()

            # Calculate total price of the order
            pedido.preco = pedido.get_total_price()
            pedido.save()

            messages.success(request, 'Pedido cadastrado com sucesso!')
            return redirect('garcomDashboard')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados.')
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
        item_formset = ItemPedidoFormSet(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.garcom = request.user
            pedido.save()
            for item_form in item_formset:
                item = item_form.save(commit=False)
                item.pedido = pedido
                item.save()
            messages.success(request, 'Pedido cadastrado com sucesso!')
            action = RecentAction(descricao=f'O garçom {request.user} criou um pedido com sucesso!')  
            action.save()
            return redirect('garcomDashboard')
        else:
            messages.error(request, 'Erro no cadastro. Verifique os dados.')
    else:
        form = PedidoForm()
    return render(request, 'novoPedido.html', {'form': form})


def garcomLogout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    action = RecentAction(descricao=f'Garçom {request.user} deslogado com sucesso!')
    action.save()
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
            action = RecentAction(descricao=f'Administrador {request.user} editado com sucesso!')
            action.save()
            return redirect("gerenciarAdministradores")
    else:
        form = AdminForm(instance=admin)
    return render(request, "editarAdministrador.html", {"form": form,"admin":admin})

@login_required
def deletarAdministrador(request, admin_id):
    admin = get_object_or_404(AdminModel, pk=admin_id)
    admin.delete()
    messages.success(request, "Administrador excluido com sucesso.")
    action = RecentAction(descricao=f'Administrador {request.user} deletou um administrador!')
    action.save()
    return redirect("gerenciarAdministradores")


@login_required
def administradorPedidos(request):
    pedidos = Pedido.objects.all()
    context = {
        'pedidos' : pedidos
    }
    return render(request,"administradorPedidos.html", context=context)


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
            action = RecentAction(descricao=f'Garçom {request.user} editado com sucesso!')
            action.save()
            return redirect("gerenciarGarcom")
    else:
        form = GarcomForm(instance=garcom)
    return render(request, "editarGarcom.html", {"form": form, "garcom":garcom})

@login_required
def deletarGarcom(request, garcom_id):
    
    garcom = get_object_or_404(GarcomModel, pk=garcom_id)
    garcom.delete()
    messages.success(request, "Garçom excluido com sucesso.")
    action = RecentAction(descricao=f'Administrador {request.user} deletou um garçom!')
    action.save()
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
            action = RecentAction(descricao=f'Cozinha {request.user} editado com sucesso!')
            action.save()
            return redirect("gerenciarCozinha")
    else:
        form = CozinhaForm(instance=cozinha)
    return render(request, "editarCozinha.html", {"form": form, "cozinha":cozinha})

@login_required
def deletarCozinha(request, cozinha_id):
    cozinha = get_object_or_404(CozinhaModel, pk=cozinha_id)
    cozinha.delete()
    messages.success(request, "Cozinha excluido com sucesso.")
    action = RecentAction(descricao=f'O administrador {request.user} deletou um Cozinha!')
    action.save()
    return redirect("gerenciarCozinha")


@login_required
def cozinhaAvancarPedido(request,pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    current_status = pedido.status
    for i, (status, _) in enumerate(Pedido.STATUS_CHOICES):
        if status == current_status:
            next_status_index = (i + 1) % len(Pedido.STATUS_CHOICES)
            pedido.status = Pedido.STATUS_CHOICES[next_status_index][0]
            break
    pedido.save()
    messages.success(request, 'Status do pedido alterado pela cozinha!')
    action = RecentAction(descricao=f'Cozinha alterou o status do pedido!')
    action.save()
    return redirect('cozinhaDashboard')



@login_required
def gerenciarCardapio(request):
    menu = ItemCardapio.objects.all()
    form = ItemCardapioForm()
    return render(request, "gerenciarCardapio.html", {"menu": menu,"form": form})


@login_required
def adicionarItemCardapio(request):
    if request.method == "POST":
        form = ItemCardapioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Item adicionado com sucesso.")
            action = RecentAction(descricao=f'Item {request.user} adicionado com sucesso!')
            action.save()
            return redirect("gerenciarCardapio")
    else:
        form = ItemCardapioForm()
    return render(request, "gerenciarCardapio.html", {"form": form})


@login_required
def editarItemCardapio(request, pk):
    item = ItemCardapio.objects.get(id=pk)
    if request.method == "POST":
        form = ItemCardapioForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item editado com sucesso.")
            action = RecentAction(descricao=f'Item {request.user} editado com sucesso!')
            action.save()
            return redirect("gerenciarCardapio")
    else:
        form = ItemCardapioForm(instance=item)
    return render(request, "editarItemCardapio.html", {"form": form, "item":item})


@login_required
def deletarItemCardapio(request, pk):
    item = get_object_or_404(ItemCardapio, id=pk)
    item.delete()
    messages.success(request, "Item excluido com sucesso.")
    action = RecentAction(descricao=f'O administrador {request.user} deletou um Item!')
    action.save()
    return redirect("gerenciarCardapio")
    

@login_required
def clean_actions(request):
    RecentAction.objects.all().delete()  # Delete all RecentAction instances
    return redirect('administradorDashboard')  # Redirect to the dashboard


@login_required
def clean_pedidos(request):
    Pedido.objects.all().delete()
    action = RecentAction(descricao=f'O adm {request.user} excluiu os pedidos!')
    return redirect('administradorDashboard')