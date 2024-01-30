from django import forms
from .models import Reunioes

class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = Reunioes
        fields = '__all__'