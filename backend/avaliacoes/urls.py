from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_avaliacoes, name='listar_avaliacoes'),
    path('pendentes/',
         views.listar_avaliacoes_pendentes,
         name='listar_avaliacoes_pendentes'
    ),

]