def get_seconds(tempo):
    temp = tempo.split(":")
    print(temp)
    return float(temp[0])*60 + float(temp[1])

tempo_teste = "02:43.22"
print(get_seconds(tempo_teste))