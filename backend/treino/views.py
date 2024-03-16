from .models import Treino, Etapa
from .serializers import TreinoSerializer, EtapaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def list_treinos(request):
    """
        função para retornar todas as instancias de Treino
    """


    pass
    """
    queryset = Teste.objects.all()
    queryset_serial = TesteSerializer(queryset, many=True)
    response = {
            "status": "sucess",
            "messagem": "todos os treinos obtidos com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": queryset_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)
    """