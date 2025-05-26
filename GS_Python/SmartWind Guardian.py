#link:
#Dupla: Ian Batinga Barbosa / Giovanna Carmona Roman Lopes

def preenchermedicao(guardian):
    resp = "S"
    while resp == "S":
        equipamento = [float(input("Digite aqui a velocidade do vento em Km/h: ")),
                       float(input("Digite aqui a direção do vento em graus de 0 a 360: ")),
                       float(input("Digite aqui a umidade do ar em porcentagem: "))]
        guardian.append(preenchermedicao)
        resp = input("Digite 'S' para continuar: ").upper()

def exibirmedicao():
    for elemento in guardian:
        print("Vel. vento(km/h)........: ", elemento[0])
        print("Direção vento (graus)...: ", elemento[1])
        print("Umidade do ar (%).......: ", elemento[2])

guardian = []
print("Preenchendo")
preenchermedicao(guardian)
print("Exibindo")
exibirmedicao(guardian)