from django.views.generic import ListView
from modulo12.models import MtgTabDatgenTgrado, MtgTabDefensa, MtgTabCorrecciones, MtgTabDesarrollodefases
from django import forms

class fase1Form(forms.ModelForm):
	class Meta:
		model = MtgTabDatgenTgrado

class defensaForm(forms.ModelForm):
	class Meta:
		model = MtgTabDefensa

class fase1ListForm(ListView):
    model = MtgTabDatgenTgrado

class correccionDocenteForm(forms.ModelForm):
    class Meta:
        model = MtgTabCorrecciones

class desarrolloForm(forms.ModelForm):
    class Meta:
        model = MtgTabDesarrollodefases

