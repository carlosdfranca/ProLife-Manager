from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name='homepage'),

    # Páginas relacionadas a área do trabalho
    path("areatrabalhador", area_trabalhador_view, name='area_trabalhador'),
    path("tarefas", tarefas_view, name='tarefas'),
    path("compromissos", compromissos_view, name='compromissos'),


    # Páginas relacionadas ao usuário
    path("fazerlogin/", fazer_login, name='fazer_login'),
    path("fazerlogout/", fazer_logout, name='fazer_logout'),
]