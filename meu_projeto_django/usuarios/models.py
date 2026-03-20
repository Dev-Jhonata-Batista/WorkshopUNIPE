from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
    

