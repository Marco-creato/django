from django.shortcuts import render

# Create your views here.

def findex(request):
    return render(request, "index.html")

def fhistoria(request):
    return render(request, "historia.html")

