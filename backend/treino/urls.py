from django.urls import path
from . import views

urlpatterns = [
   path('list_treinos/', views.list_treinos),
   path('create_treino/', views.create_treino),
   path('create_tipo/', views.create_tipo),
   path('get_tipos/', views.get_tipos),
   path('get_etapas/', views.get_etapas),
   path('get_treino/<int:id>/', views.get_treino),
   path('get_treino_tipo/<int:id_tipo>/', views.get_treino_tipo),
]