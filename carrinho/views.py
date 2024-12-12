from django.shortcuts import render, redirect
from django.contrib import messages
from produto.models import Produto
from cliente.models import Cliente
from .models import itemCarrinho

# Create your views here.

def addcarrinho(request, produto_id):
    if request.method == 'POST':
        try:
            produto = Produto.objects.get(id=produto_id)  # Certifique-se de que o nome do modelo é Produto
            quantidade = int(request.POST.get('quantidade', 1))  # Pega a quantidade, ou 1 como padrão

            cliente_id = request.session.get('cliente_id')  # Verifica se o cliente está logado
            if cliente_id:
                cliente = Cliente.objects.get(id=cliente_id)
                # Cria o item no carrinho
                itemCarrinho.objects.create(cliente=cliente, produto=produto, quantidade=quantidade)
                messages.success(request, 'Produto adicionado ao carrinho.')
                return redirect('carrinho')  # Redireciona para a página do carrinho (ajuste conforme necessário)
            else:
                messages.error(request, 'Você precisa estar logado para adicionar produtos ao carrinho.')
                return redirect('flogin')  # Redireciona para a página de login (ajuste conforme necessário)
        except Produto.DoesNotExist:
            messages.error(request, 'Produto não encontrado.')
            return redirect('findex')  # Redireciona para a página inicial ou uma página de erro
        except Exception as e:
            messages.error(request, f'Ocorreu um erro inesperado: {str(e)}')
            return redirect('findex')  # Redireciona para uma página de erro genérico
    else:
        return redirect('findex')  # Redireciona caso o método não seja POST

def exibir_carrinho(request):
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
        itens = itemCarrinho.objects.filter(cliente_id=cliente_id)
        total = sum(item.total_preco() for item in itens)
        return render(request, 'carrinho.html', {'itens': itens, 'total': total})
    else:
        messages.error(request, 'Você precisa estar logado para ver o carrinho.')
        return render(request, "login.html")

def carrinho(request):
    return render(request, "carrinho.html")
