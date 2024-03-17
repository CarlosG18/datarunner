from .models import Treino, Etapa, Tipo
from .serializers import TreinoSerializer, EtapaSerializer, TipoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import re

def get_seconds(tempo):
    temp = tempo.split(":")
    return float(temp[0])*60 + float(temp[1])

def get_tempos(dados):
    dados_tempos = []
    tipo_treino = Tipo.objects.get(id=dados["tipo"])
    data = re.findall(r'\d{2}:\d{2}\.\d{2}', dados["tempos"])
    for index, tempo in enumerate(data):
        data[index] = get_seconds(tempo)

    print(data)
    data_tempo = []
    for i in range(0,len(data)-1,2):
        data_tempo.append([
            data[i], data[i+1]
        ])
    
    if tipo_treino.modo == "intervalado" or tipo_treino.modo == "subida":
        for index, tempos in enumerate(data_tempo):
            if index % 2 == 0:
                descricao = "corrida"
            else:
                descricao = "descanco"
            dict_etapa = {
                "distancia": tipo_treino.distancia_corrida,
                "tempo_corrido": tempos[0],
                "tempo_exato": tempos[1],
                "descricao": descricao,
                "treino": dados["treino"],
            }
            dados_tempos.append(dict_etapa)

    elif tipo_treino.modo == "direto":
        for tempos in data_tempo:
            dict_etapa = {
                "distancia": tipo_treino.distancia_corrida,
                "tempo_corrido": tempos[0],
                "tempo_exato": tempos[1],
                "descricao": "corrida",
                "treino": dados["treino"],
            }
            dados_tempos.append(dict_etapa)

    return dados_tempos

@api_view(['GET'])
def get_etapas(request):
    queryset = Etapa.objects.all()
    queryset_serial = EtapaSerializer(queryset, many=True)
    response = {
            "status": "sucess",
            "messagem": "todos as etapas obtidas com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": queryset_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_treinos(request):
    queryset = Treino.objects.all()
    queryset_serial = TreinoSerializer(queryset, many=True)
    response = {
            "status": "sucess",
            "messagem": "todos os treinos obtidos com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": queryset_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_tipos(request):
    queryset = Tipo.objects.all()
    queryset_serial = TipoSerializer(queryset, many=True)
    response = {
            "status": "sucess",
            "messagem": "todos os tipos obtidos com sucesso!",
            "code": status.HTTP_200_OK,
            "dados": queryset_serial.data
        }
    return Response(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_treino(request):
    data = request.data
    data_serial = TreinoSerializer(data=data)
    if data_serial.is_valid():
        response = {
            "status": "sucess",
            "messagem": "treino criado com sucesso!",
            "code": status.HTTP_201_CREATED,
            "dados": data
        }
        data_serial.save()
        dados_tempo = {
            "tempos": data["dados_tempo"],
            "tipo": data["tipo"],
            "treino": Treino.objects.latest('id'),
        }
        data_etapa = get_tempos(dados_tempo)
        for dado in data_etapa:
            etapa = Etapa(treino=dado["treino"], distancia=dado["distancia"], tempo_corrido=dado["tempo_corrido"], tempo_exato=dado["tempo_exato"],descricao=dado["descricao"])
            etapa.save()        
    else:
        return Response(data_serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_tipo(request):
    data = request.data
    data_serial = TipoSerializer(data=data)
    if data_serial.is_valid():
        response = {
            "status": "sucess",
            "messagem": "tipo de treino criado com sucesso!",
            "code": status.HTTP_201_CREATED,
            "dados": data
        }
        data_serial.save()
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(data_serial.errors, status=status.HTTP_400_BAD_REQUEST)