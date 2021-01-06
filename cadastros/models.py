from django.db import models

# Create your models here.

class Genero(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo


class Filme(models.Model):

    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, default=0)
    diretor = models.CharField(max_length=100, default="")
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluguel(models.Model):

    filme = models.ForeignKey(Filme, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    inicio = models.DateField(verbose_name='Data de Locação')
    fim = models.DateField(verbose_name='Data de Devolução')

    def __str__(self):
        return self.filme
