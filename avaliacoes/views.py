from django.shortcuts import render, HttpResponseRedirect
from avaliacoes.forms import AvaliacaoForm, LoginForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
from avaliacoes.models import Avaliacao, Usuario

def index(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form})


@login_required()
def avaliacao(request):
	form = AvaliacaoForm()
	return render(request, 'avaliacao.html', {'form': form})


def validar_cadastro(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            usuario = Usuario(
                username=form.data['login'],
                is_active=False)

            usuario.set_password(form.data['senha'])
            usuario.save()


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			pessoa = authenticate(username=form.data['login'], password=form.data['senha'])

			if pessoa is not None:
				if pessoa.is_active:
					meu_login(request, pessoa)
					return HttpResponseRedirect('/avaliacao/')
				else:
					return render(request, 'index.html', {'form': form})
			else:
				return render(request, 'index.html', {'form': form})
		else:
			return render(request, 'index.html', {'form': form})
	else:
		return HttpResponseRedirect('/')
