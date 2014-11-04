from django import forms
from avaliacoes.models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
	class Meta:
		model = Avaliacao