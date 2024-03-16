from django.urls import path
from . import views

urlpatterns = [
   path('list_treinos/', views.list_treinos),
   path('create_treino/', views.create_treino),
   path('create_tipo/', views.create_tipo),
   path('get_tipos/', views.get_tipos),
   path('get_etapas/', views.get_etapas),
]