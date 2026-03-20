from django import form
from .models import Usuario

class UsuarioForm(form.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'idade', 'telefone']
