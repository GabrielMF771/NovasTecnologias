n = int(input("Digite um número inteiro: "))

if n < 0:
    print("Erro: não existe fatorial de número negativo.")
else:
    resultado = 1
    for k in range(1, n + 1):
        resultado *= k
        if resultado > 1_000_000:
            print(f"Passou do limite em {k}!")
            print(f"Valor acumulado até estourar: {resultado}")
        break
    else:
        print(f"{n}! = {resultado}")