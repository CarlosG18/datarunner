import streamlit as st
import requests as re

response = re.get("http://127.0.0.1:8000/treino/list_treinos/")

response_tipos = re.get("http://127.0.0.1:8000/treino/get_tipos/")
tipos = [tipo["modo"]+" "+str(tipo["distancia_corrida"])+"/"+str(tipo["distancia_descanco"]) for tipo in response_tipos.json()["dados"]]

dict_tipo = {}

for i in response_tipos.json()["dados"]:
    dict_tipo[tipos[i["id"]-1]] = i["id"]

print(dict_tipo)

tela = 0

st.title("DATARUNNER")
st.sidebar.text("")
opcao = st.sidebar.selectbox("escolha uma opção", options=["adicionar dados", "visualizar dados", "criar novos treinos"])


if opcao == "adicionar dados":
    tela = 0
elif opcao == "visualizar dados":
    tela = 1
else:
    tela = 2

if tela == 0:
    st.text("tipos de treinos")
    opcao = st.selectbox("escolha uma opção", options=dict_tipo)
    #st.write("id escolhido =",dict_tipo[opcao])
    st.divider()

    st.text("informe o nome do treino:")
    titulo = st.text_input("insira aqui", key="titulo")
    st.divider()
    
    st.text("data do treino:")
    data = st.date_input("data")
    st.divider()

    st.text("distância total do treino:")
    distancia = st.number_input("distancia total")
    st.divider()
    
    st.text("informe os dados do treino:")
    dados_tempo = st.text_area("insira aqui", key="dados")
    button_send = st.button("enviar")

    dict_create_treino = {
        "titulo": titulo,
        "data": str(data.year)+"-"+str(data.month)+"-"+str(data.day),
        "distancia_total": distancia,
        "tipo": dict_tipo[opcao],
        "dados_tempo": dados_tempo, 
    }
    
    if button_send:
        st.write("butao enviar apertado")
        st.write(dict_create_treino)
        request = re.post("http://127.0.0.1:8000/treino/create_treino/", data=dict_create_treino)
        st.write(request.json())
elif tela == 1:
    st.write(response.json()["dados"])
else:
    modos_tipo = [
        "intervalado",
        "direto",
        "subida",
    ]

    st.text("informe o modo do treino:")
    modo = st.selectbox("escolha o modo do treino:", options=modos_tipo)
    st.text("informe os dados do treino:")
    dist_corrida = st.number_input("distância de corrida", key="distancia_corrida")
    dist_descanco = st.number_input("distância de descanco", key="distancia_descanco")
    dict_create_tipo = {
        "modo": modo,
        "distancia_corrida": float(dist_corrida),
        "distancia_descanco": float(dist_descanco),
    }

    button_send = st.button("enviar")
    if button_send:
        st.write(dict_create_tipo)
        request = re.post("http://127.0.0.1:8000/treino/create_tipo/", data=dict_create_tipo)
        st.write(request.json())



