from django.contrib import admin
from .models import Livro

class ListLivros(admin.ModelAdmin):
    list_display = ('nome_livro','nome_autor','nome_editora','ano_publicacao','quantidade_paginas', 'preco',)

admin.site.register(Livro, ListLivros)
