from django.contrib.auth.models import User
from django.forms import ModelForm
from django.views.generic import ListView
from modulo12.models import *
from django import forms


#LOGIN DE USUARIOS

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

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

class versionamientoForm(forms.ModelForm):
    class Meta:
        model = MtgTabVersionamiento

class fasesForm(forms.ModelForm):
    class Meta:
        model = MtgTabFases

class juradoForm(forms.ModelForm):
    class Meta:
        model = MtgTabJurados

########################################### REGISTRO
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }