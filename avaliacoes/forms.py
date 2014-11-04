from django import forms
from avaliacoes.models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
	class Meta:
		model = Avaliacao

class LoginForm(forms.Form):
	login = forms.CharField(max_length=100, required=True)
	senha = forms.CharField(widget=forms.PasswordInput, required=True)
