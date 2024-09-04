from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Gosto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
