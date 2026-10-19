from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Avaliacao(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('RESPONDIDA', 'Respondida'),
    ]

    nota = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    comentario = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='PENDENTE'
    )

    data_criacao = models.DateTimeField(auto_now_add=True)

    aluno = models.ForeignKey(
        'alunos.Aluno',
        on_delete=models.CASCADE,
        related_name='avaliacoes'
    )

    disciplina = models.ForeignKey(
        'disciplinas.Disciplina',
        on_delete=models.CASCADE,
        related_name='avaliacoes'
    )

    def __str__(self):
        return f'{self.aluno} - {self.disciplina}'
    