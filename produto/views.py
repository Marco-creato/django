from django.shortcuts import render, redirect

# Create your views here.

from .models import Produto

def fproduto(request):
    produtos = Produto.objects.all()
    return render(request, "rel_produto.html", {"produtos":produtos})

def fcadproduto(request):
    return render(request, "cad_produto.html")


def salvar(request):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    vimagem = request.FILES.get("imagem")
    if vnome:
        Produto.objects.create(
            nome=vnome,
            descricao=vdescricao,
            preco=vpreco,
            quantidade=vquantidade,
            imagem=vimagem
        )
    return redirect(fproduto)


def exibir(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "update.html", {"produto": produto})



def excluir(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(fproduto)

def update(request, id):
    vnome = request.POST.get("nome")
    vdescricao = request.POST.get("descricao")
    vpreco = request.POST.get("preco")
    vquantidade = request.POST.get("quantidade")
    vimagem = request.FILES.get("imagem")

    produto = Produto.objects.get(id=id)
    produto.nome = vnome
    produto.descricao = vdescricao
    produto.preco = vpreco
    produto.quantidade = vquantidade
    if vimagem:
        produto.imagem = vimagem
    produto.save()
    return redirect(fproduto)


def celulares(request):
    return render(request, "celulares.html")



