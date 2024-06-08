from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def homepage(request):
    
    return render(request, 'homepage.html')















# Aqui vão ficar os views de autenticação e edição do usuário
def fazer_login(request):
    erro = None
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        dados = request.POST.dict()
        if "username" in dados and "password" in dados:
            username = dados.get("username")
            password = dados.get("password")
            usuario = authenticate(request, username=username, password=password)
            if usuario:
                login(request, usuario)
                return redirect("homepage")
            else:
                erro = "credenciais"
        else:
            erro = "preenchimento"
    
    context = {
        "erro": erro
    }

    return render(request, 'auth/login.html', context)


@login_required
def fazer_logout(request):
    logout(request)
    return redirect('fazer_login')