from rest_framework import serializers
from inss.models import MeuInss

class MeuInssSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeuInss
        fields = '__all__'