from rest_framework import viewsets
from .serializers import ReuniaoSerializer
from reunioes.models import Reunioes

class ReuniaoViewSet(viewsets.ModelViewSet):
    queryset = Reunioes.objects.all()
    serializer_class =  ReuniaoSerializer