from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name='homepage'),


    # Páginas relacionadas ao usuário
    path("fazerlogin/", fazer_login, name='fazer_login'),
    path("fazerlogout/", fazer_logout, name='fazer_logout'),
]