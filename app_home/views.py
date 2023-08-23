from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'index.html')

def usuarios(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #Exibir todos usuarios cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a listagem de usuários
    return render(request, 'usuarios.html', usuarios)
