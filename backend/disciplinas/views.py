from django.http import JsonResponse
from .models import Disciplina

def listar_disciplinas(request):
    disciplinas = list(Disciplina.objects.values())
    return JsonResponse(disciplinas, safe=False)

