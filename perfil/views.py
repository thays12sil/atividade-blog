from django.shortcuts import render
from .models import Curso, Gosto

def index(request):
    cursos = Curso.objects.all()
    gostos = Gosto.objects.all()
    context = {
        'cursos': cursos,
        'gostos': gostos
    }
    return render(request, 'index.html', context)

def sobre(request):
    context = {
        'foto_url': './foto.png',  # Substitua pelo caminho correto da sua imagem
    }
    return render(request, 'sobre.html', context)

    