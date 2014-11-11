from django.shortcuts import render, HttpResponseRedirect
from avaliacoes.forms import AvaliacaoForm, LoginForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
from avaliacoes.models import Avaliacao, Usuario
from decimal import Decimal

def index(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form})


@login_required()
def avaliacao(request):
	form = AvaliacaoForm()
	avaliacoes = Avaliacao.objects.all()
	return render(request, 'avaliacao.html', {'form': form, 'avaliacoes': avaliacoes})


def validar_cadastro(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            usuario = Usuario(
                username=form.data['login'],
                is_active=True)

            usuario.set_password(form.data['senha'])
            usuario.save()

            form = LoginForm()
            return render(request, 'index.html', {'form': form})


def calcular(request):
	if request.method == 'POST':
		form = AvaliacaoForm(request.POST)
		altura = Decimal(form.data['altura'])
		peso = Decimal(form.data['peso'])
		calculo = peso / (altura * altura)
		if calculo < 18.5:
			resultado = 'Abaixo do peso ideal - '
		elif calculo > 18.5 and calculo < 24.9:
			resultado = 'Peso ideal - '
		elif calculo > 24.9 and calculo < 29.9:
			resultado = 'Sobrepeso - '
		elif calculo > 29.9 and calculo < 34.9:
			resultado = 'Obesidade Grau I - '
		elif calculo > 34.9 and calculo < 39.9:
			resultado = 'Obesidade Grau II - '
		elif calculo > 39.9:
			resultado = 'Obesidade Grau III - '

		avaliacao = Avaliacao()
		avaliacao.nome = form.data['nome']
		avaliacao.idade = form.data['idade']
		avaliacao.sexo = form.data['sexo']
		avaliacao.altura = altura
		avaliacao.peso = peso
		avaliacao.resultado = calculo
		avaliacao.save()

		return render(request, 'avaliacao.html', {'form': form, 'calculo': calculo,'resultado': resultado})
	else:
		form = LoginForm()
        return render(request, 'index.html', {'form': form})

def apagar(request, pk=0):
    try:
        avaliacao = Avaliacao.objects.get(pk=pk)
        avaliacao.delete()
        return HttpResponseRedirect('/avaliacao/')
    except:
        return HttpResponseRedirect('/avaliacao/')


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

def fazerLogoff(request):
	logout(request)
	return HttpResponseRedirect('/')

def cadastroUsuario(request):
	formLogin = LoginForm()
	return render(request, 'cadastroUsuario.html', {'formLogin': formLogin})
