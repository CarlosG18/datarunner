from django.db import models

# Create your models here.
class Treino(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    distancia_total = models.FloatField()

    def __str__(self):
        return f'Treino {self.titulo} com distancia total de {self.distancia_total} realizado na data {self.data}'

class Etapa(models.Model):
    tipos_etapa = [
        "Corrida",
        "Descanço",
        "Caminhar",
    ]
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    distancia = models.FloatField()
    tempo_corrido = models.TimeField()
    tempo_exato = models.TimeField()
    descricao = models.CharField(max_length=100, choices=[(tipo,tipo) for tipo in tipos_etapa])

    def __str__(self):
        return f'Etapa {self.distancia} km do treino {self.treino.titulo} - tempo exato: {self.tempo_exato} - tipo: {self.descricao}'

