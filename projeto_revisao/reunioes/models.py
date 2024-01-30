from django.db import models

class Reunioes(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.TextField()
    local = models.CharField(max_length=50)
    nome_participante = models.CharField( max_length=120)
    data = models.DateField(auto_now_add=False)


    def __str__(self):
        return self.titulo