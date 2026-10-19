from django.db import models

# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    professor = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome 