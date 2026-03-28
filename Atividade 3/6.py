tamanho = 1000
primos = [1] * tamanho
primos[0] = primos[1] = 0

for i in range(2, tamanho):
    if primos[i] == 1:
        for j in range(i * 2, tamanho, i):
            primos[j] = 0

print("Números primos entre 2 e 999:")
contador = 0

for indice in range(2, tamanho):
    if primos[indice] == 1:
        print(f"{indice:3}", end=" ")
        contador += 1
        if contador % 15 == 0:
            print()

print(f"\n\nTotal de números primos encontrados: {contador}")