from django.db import models

# Create your models here.

class Filme(models.Model):

    GENERO_ACAO = 'Ação'
    GENERO_COMEDIA = 'Comédia'
    GENERO_DRAMA = 'Drama'
    GENERO_TERROR = 'Terror'
    GENERO_FICCAO = 'Ficção'

    GENERO_CHOICES = [
        (GENERO_ACAO, 'Ação'),
        (GENERO_COMEDIA, 'Comédia'),
        (GENERO_DRAMA, 'Drama'),
        (GENERO_TERROR, 'Terror'),
        (GENERO_FICCAO, 'Ficção'),
    ]

    titulo = models.CharField(max_length=100)
    ano = models.IntegerField(blank=True, default=0)
    diretor = models.CharField(max_length=100, default="")
    genero = models.CharField(choices=GENERO_CHOICES, max_length=10, default=GENERO_ACAO)

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
