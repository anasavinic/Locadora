from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from cadastros.forms import FilmeForm, ClienteForm, AluguelForm, GeneroForm
from cadastros.models import Filme, Cliente, Aluguel, Genero


def lista_genero(request):

    qs = Genero.objects.filter()

    context = {
        'genero': qs,
    }

    return render(request, 'cadastros/lista_genero.html', context)


def detalhe_genero(request, id):

    genero = get_object_or_404(Genero, pk=id)

    filme_mostrar = Filme.objects.filter(genero_id=genero)

    context = {
        'genero': genero,
        'filme_mostrar': filme_mostrar,
    }

    return render(request, 'cadastros/detalhe_genero.html', context)


def cadastrar_genero(request):

    if request.method == 'POST':
        form = GeneroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('genero-list')
    else:
        form = GeneroForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastros/cadastrar_genero.html', context)


def lista_filmes(request):

    qs = Filme.objects.filter()

    context = {
        'filmes': qs,
    }

    return render(request, 'cadastros/lista_filmes.html', context)


def detalhe_filmes(request, id):

    filme = get_object_or_404(Filme, pk=id)

    context = {
        'filmes': filme,
    }

    return render(request, 'cadastros/detalhe_filmes.html', context)


def cadastrar_filmes(request):

    if request.method == 'POST':
        form = FilmeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('filmes-list')
    else:
        form = FilmeForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastros/cadastrar_filmes.html', context)


def remove_filmes(request, id):

    filme = get_object_or_404(Filme, pk=id)

    filme.delete()

    return redirect('filmes-list')


def lista_cliente(request):

    qs = Cliente.objects.all()

    context = {
        'clientes': qs,
    }

    return render(request, 'cadastros/lista_cliente.html', context)


def detalhe_cliente(request, id):

    cliente = get_object_or_404(Cliente, pk=id)

    context = {
        'clientes': cliente,
    }

    return render(request, 'cadastros/detalhe_cliente.html', context)


def cadastrar_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('cliente-list')
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastros/cadastrar_cliente.html', context)


def remove_cliente(request, id):

    cliente = get_object_or_404(Cliente, pk=id)

    cliente.delete()

    return redirect('cliente-list')


def lista_aluguel(request):

    qs = Aluguel.objects.all()

    context = {
        'aluguel': qs,
    }

    return render(request, 'cadastros/lista_aluguel.html', context)


def detalhe_aluguel(request, id):

    aluguel = get_object_or_404(Aluguel, pk=id)

    context = {
        'aluguel': aluguel,
    }

    return render(request, 'cadastros/detalhe_aluguel.html', context)


def cadastrar_aluguel(request):

    if request.method == 'POST':
        form = AluguelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('aluguel-list')
    else:
        form = AluguelForm()

    context = {
        'form': form,
    }

    return render(request, 'cadastros/cadastrar_aluguel.html', context)


def remove_aluguel(request, id):

    aluguel = get_object_or_404(Aluguel, pk=id)

    aluguel.delete()

    return redirect('aluguel-list')