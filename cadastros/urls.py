from django.urls import include, path
from cadastros.views import lista_filmes, detalhe_filmes, cadastrar_filmes, remove_filmes, lista_cliente, \
    detalhe_cliente, remove_cliente, cadastrar_cliente, lista_aluguel, detalhe_aluguel, cadastrar_aluguel, \
    remove_aluguel, lista_genero, cadastrar_genero, detalhe_genero

urlpatterns = [
    path('genero/', include([
        path('', lista_genero, name='genero-list'),
        path('detalhe/<int:id>/', detalhe_genero, name='genero-detail'),
        path('create/', cadastrar_genero, name='genero-create'),
    ])),

    path('filmes/', include([
        path('', lista_filmes, name='filmes-list'),
        path('detalhe/<int:id>/', detalhe_filmes, name='filmes-detail'),
        path('remove/<int:id>/', remove_filmes, name='filmes-remove'),
        path('create/', cadastrar_filmes, name='filmes-create'),
    ])),

    path('cliente/', include([
        path('', lista_cliente, name='cliente-list'),
        path('detalhe/<int:id>/', detalhe_cliente, name='cliente-detail'),
        path('remove/<int:id>/', remove_cliente, name='cliente-remove'),
        path('create/', cadastrar_cliente, name='cliente-create'),
    ])),

    path('aluguel/', include([
        path('', lista_aluguel, name='aluguel-list'),
        path('detalhe/<int:id>/', detalhe_aluguel, name='aluguel-detail'),
        path('remove/<int:id>/', remove_aluguel, name='aluguel-remove'),
        path('create/', cadastrar_aluguel, name='aluguel-create'),
    ])),
]