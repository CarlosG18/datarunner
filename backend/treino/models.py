from django.db import models

# Create your models here.
class Tipo(models.Model):
    modos_tipo = [
        "intervalado",
        "direto",
        "subida",
    ]
    modo = models.CharField(max_length=200, choices=[(tipo,tipo) for tipo in modos_tipo])
    distancia_corrida = models.FloatField()
    distancia_descanco = models.FloatField()

    def __str__(self):
        return f'treino do tipo {self.modo} - {self.distancia_corrida}/{self.distancia_descanco}'

class Treino(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    distancia_total = models.FloatField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

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
    tempo_corrido = models.CharField(max_length=100)
    tempo_exato = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, choices=[(tipo,tipo) for tipo in tipos_etapa])

    def __str__(self):
        return f'Etapa {self.distancia} km do treino {self.treino.titulo} - tempo exato: {self.tempo_exato} - tipo: {self.descricao}'

