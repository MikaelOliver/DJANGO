from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reunioes
from .forms import ReuniaoForm

def delete(request, id):
    reunioes_marcadas = Reunioes.objects.get(id=id)
    if request.method == 'POST':
        reunioes_marcadas.delete()
        return redirect('/')
    return render(request, 'reunioes/delete.html')

def index(request):
    reunioes = Reunioes.objects.all()
    return render(request,'reunioes/index.html',{'reunioes': reunioes})

def register(request):
    if request.method == "POST":
        form = ReuniaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reunião Cadastrada')
            form = ReuniaoForm()
        else:
            messages.error(request,'Error ao cadastrar a reunião')
    else:
        form = ReuniaoForm()
    
    return render(request,'reunioes/register.html',{ 'form' : form })