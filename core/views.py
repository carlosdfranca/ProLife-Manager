from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from trabalho.models import *

# Create your views here.
@login_required
def homepage(request):
    
    return render(request, 'homepage.html')


# Trabalho
@login_required
def tarefas_view(request):
    user = request.user

    tarefas = Tasks.objects.filter(user=user)

    context = {
        "tarefas": tarefas
    }

    return render(request, 'trabalho/tarefas.html', context)


@login_required
def compromissos_view(request):
    
    return render(request, 'trabalho/compromissos.html')

@login_required
def area_trabalhador_view(request):
    
    return render(request, 'trabalho/area_trabalhador.html')



# Pessoal
def dieta_view(request):

    return render(request, "pessoal/dieta.html")


def lista_comrpas_view(request):

    return render(request, "pessoal/lista_comrpas.html")


def lista_desejos_view(request):

    return render(request, "pessoal/lista_desejos.html")


def plano_academia_view(request):

    return render(request, "pessoal/plano_academia.html")


def area_pessoal_view(request):

    return render(request, "pessoal/area_pessoal.html")



# Objetivos
def area_objetivos_view(request):

    return render(request, "objetivos/area_objetivos.html")



# Financeiro
def carteiras_view(request):

    return render(request, "financeiro/carteiras.html")


def despesas_view(request):

    return render(request, "financeiro/despesas.html")


def receitas_view(request):

    return render(request, "financeiro/receitas.html")


def area_financeiro_view(request):

    return render(request, "financeiro/area_financeiro.html")



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