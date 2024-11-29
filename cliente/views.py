from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.hashers import make_password
from django.contrib import messages

# Create your views here.

def fcliente(request):
    clientes = Cliente.objects.all()
    return render(request, "rel_cliente.html",{"clientes":clientes})

def Fcadcliente(request):
    return render(request, "cad_cliente.html")

def salvar_cli(request):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    vsenha = request.POST.get("senha")

    senha_criptografada = make_password(vsenha)
    if vnome:
        Cliente.objects.create(nome=vnome, telefone=vtelefone, email=vemail, senha=senha_criptografada)
    return redirect(fcliente)

def exibir_cli(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "update_cli.html", {"cliente": cliente})


def excluir_cli(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect(fcliente)

def update_cli(request, id):
    vnome = request.POST.get("nome")
    vtelefone = request.POST.get("telefone")
    vemail = request.POST.get("email")
    cliente = Cliente.objects.get(id=id)
    cliente.nome = vnome
    cliente.telefone = vtelefone
    cliente.email = vemail
    cliente.save()
    return redirect(fcliente)

def ftelacliente(request):
    return render(request, "telacliente.html")

def flogin(requets):
    return render(requets, "login.html")

def logar(request):
    if request.method == 'POST':
        email = request.POST.get("username")
        senha = request.POST.get("password")

        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.check_password(senha):
                return redirect('ftelacliente')
            else:
                return redirect('flogin')
        except Cliente.DoesNotExist:
            messages.error(request, 'Credencias invalidas.')











