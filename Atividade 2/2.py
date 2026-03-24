import math
hora = int(input("Digite a hora: (0-23)\n"))
chuva = int(input("Está chovendo? (0-1)\n"))
fluxo = int(input("Qual o nível do fluxo? (0 - baixo, 1 - médio, 2 - alto)\n"))

if ((hora in range(7,9) or hora in range(17,19))):
    tempo_base = 60
else:
    tempo_base = 35
if(chuva == 1):
    tempo_base *= 1.2
if(fluxo == 2):
    tempo_base += 15
if(fluxo == 0):
    tempo_base -= 10

print(f"O tempo base esperado é: {math.ceil(tempo_base)}")