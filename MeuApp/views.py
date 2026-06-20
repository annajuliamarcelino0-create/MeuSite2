from multiprocessing import context
from urllib import request

from django.shortcuts import render

# Create your views here.
def home(request):
    
    #variaveis que eu vou enviar para o template
    context = {
        'nome': 'Anna',
        'sobrenome': 'Oliveira',
    }
    
    
    # o segundo parametro e o caminho do html 
    return render(request, 'home.html', context)


def contato(request):
    return render(request, 'contato.html')


 
def exibir_produtos(request):
    produtos = [
        {'nome': 'Produto 1', 'preco': 10.99},
        {'nome': 'Produto 2', 'preco': 20.99},
        {'nome': 'Produto 3', 'preco': 30.99},
    ]
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos.html', context)
 