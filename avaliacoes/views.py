from django.shortcuts import render
from avaliacoes.forms import AvaliacaoForm, LoginForm
from django.contrib.auth.decorators import login_required
from avaliacoes.models import Avaliacao, Usuario



def validar_cadastro(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            usuario = Usuario(
                username=form.data['login'],
                is_active=False)

            usuario.set_password(form.data['senha'])
            usuario.save()
