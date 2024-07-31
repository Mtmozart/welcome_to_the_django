from django.db import models
from datetime import datetime

# Create your models here.
class Fotografia(models.Model):
     
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=150, choices=OPCOES_CATEGORIA, default='')
    descrição = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=200, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia nome=[{self.nome}]'

    