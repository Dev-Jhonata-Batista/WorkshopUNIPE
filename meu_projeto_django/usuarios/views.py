from django.shortcuts import render, redirect

from django.shortcuts import render
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/list.html', {'usuarios': usuarios})


from meu_projeto_django.usuarios.models import Usuario
from .form import UsuarioForm

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form.html', {'form': form})

def atualizar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/form.html', {'form': form})

def deletar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/confirmar_delete.html', {'usuario': usuario})

