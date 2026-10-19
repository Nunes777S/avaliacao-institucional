from django.http import JsonResponse

# Create your views here.

from .models import Aluno

def listar_alunos(request):
    alunos = list(Aluno.objects.values())
    return JsonResponse(alunos, safe=False)