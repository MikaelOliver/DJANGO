from rest_framework import viewsets
from .serializers import MeuInssSerializer
from inss.models import MeuInss

class MeuInssViewSet(viewsets.ModelViewSet):
    queryset = MeuInss.objects.all()
    serializer_class = MeuInssSerializer