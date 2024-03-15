from django.db import models

# Create your models here.
class Tipo(models.Model):
    distancia_total = models.FloatField()
    
    def __str__(self):
        return f'Tipo de treino {self.distancia_total}'

class Treino(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Treino {self.titulo} realizado na data {self.data}'

class Etapa(models.Model):
    tipos_etapa = [
        "Corrida",
        "Descanço",
        "Caminhar",
    ]

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    distancia = models.FloatField()
    tempo_corrido = models.TimeField()
    tempo_exato = models.TimeField()
    descricao = models.CharField(max_length=200, choices=[(tipo,tipo) for tipo in tipos_etapa])

    def __str__(self):
        return f'Etapa {self.distancia} - tempo exato: {self.tempo_exato} - tipo: {self.descricao}'


