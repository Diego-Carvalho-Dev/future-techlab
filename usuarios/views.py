from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter 7 ou mais digitos')
            return redirect('/usuarios/cadastro')
        
        try:
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha
            )

            messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso')
        except:
            messages.add_message(request, constants.ERROR, 'Erro do sistema, contate ao administrador!')
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/login')
    
from django.contrib.auth import authenticate, login

def logar(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(username=username, password=senha)
        
        if user is not None:
            login(request, user)  # Log the user in
            return redirect("/exames/solicitar_exames/")
        else:
            messages.add_message(request, constants.ERROR, "Usuario ou senha inválidos")
            return redirect("/usuarios/login")