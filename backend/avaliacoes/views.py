from django.http import JsonResponse
from .models import Avaliacao

def listar_avaliacoes(request):
    avaliacoes = list(Avaliacao.objects.values ())
    return JsonResponse(avaliacoes, safe=False)


def listar_avaliacoes_pendentes(request):
    avaliacoes = list(
        Avaliacao.objects.filter(status='PENDENTE').values()

    )
    return JsonResponse(avaliacoes, safe=False)


# Create your views here.
