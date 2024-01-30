from rest_framework import serializers
from reunioes.models import Reunioes


class ReuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reunioes
        fields = '__all__'