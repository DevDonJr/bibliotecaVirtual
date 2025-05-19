from django.db import models
from datetime import date

class Livros(models.Model):
    pass
    
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    categoria = models.CharField(max_length=100)
    data_cadastro= models.DateField(default = date.today)
    data_emprestimo = models.DateField(null=True, blank=True)
    data_devolucao = models.DateField(null=True, blank=True)
    nome_emprestado = models.CharField(max_length=30, blank=True) 
    tempo_duracao= models.IntegerField(blank=True)
    disponivel = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Livro'
        
    def __str__(self):
        return self.titulo