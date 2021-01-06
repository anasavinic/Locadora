from django import forms
from django.forms import DateTimeInput, DateInput
import django.forms.widgets
import datetime

from cadastros.models import Filme, Cliente, Aluguel


class FilmeForm(forms.ModelForm):

    class Meta:
        model = Filme
        fields = '__all__'


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class AluguelForm(forms.ModelForm):

    inicio = forms.CharField(widget=DateInput())
    fim = forms.CharField(widget=DateInput())

    class Meta:
        model = Aluguel
        fields = '__all__'