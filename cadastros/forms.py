from django import forms
from django.forms import DateInput

from cadastros.models import Filme, Cliente, Aluguel, Genero


class GeneroForm(forms.ModelForm):

    class Meta:
        model = Genero
        fields = "__all__"


class FilmeForm(forms.ModelForm):

    class Meta:
        model = Filme
        fields = '__all__'


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class AluguelForm(forms.ModelForm):

    inicio = forms.CharField(widget=DateInput(), help_text='Entre com a Data no Seguinte Formato: AAAA-MM-DD')
    fim = forms.CharField(widget=DateInput(), help_text='Entre com a Data no Seguinte Formato: AAAA-MM-DD')

    class Meta:
        model = Aluguel
        fields = '__all__'