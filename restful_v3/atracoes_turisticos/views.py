from django.shortcuts import render
from atracoes_turisticos.models import AtracaoTuristica

def index(request):
    atracoes_turisticos = AtracaoTuristica.objects.all()

    return render(request, 'atracoes_turisticos/index.html', {'atracoes_turisticos' : atracoes_turisticos })

