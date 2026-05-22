from datetime import datetime

data1_str = input("Digite a primeira data (DD/MM/AAAA): ")
data2_str = input("Digite a segunda data (DD/MM/AAAA): ")

data1 = datetime.strptime(data1_str, "%d/%m/%Y")
data2 = datetime.strptime(data2_str, "%d/%m/%Y")

diferenca = abs((data2 - data1).days)

semanas = diferenca // 7
dias_restantes = diferenca % 7

if data1 > data2:
    maior = data1_str
elif data2 > data1:
    maior = data2_str
else:
    maior = "As duas datas são iguais"

print("\nResultado:")
print(f"Diferença em dias: {diferenca} dias")
print(f"Diferença: {semanas} semanas e {dias_restantes} dias")
print(f"Data maior: {maior}")