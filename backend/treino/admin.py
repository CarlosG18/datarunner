from django.contrib import admin
from .models import Treino, Etapa, Tipo

# Register your models here.
admin.site.register(Treino)
admin.site.register(Tipo)
admin.site.register(Etapa)

