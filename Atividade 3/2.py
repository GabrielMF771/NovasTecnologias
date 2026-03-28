def filtrar_frequencias(lista, minimo):
    frequencias = {}

    for num in lista:
        if num in frequencias:
            frequencias[num] += 1
        else:
            frequencias[num] = 1
    resultado = []
    for num, freq in frequencias.items():
        if freq > minimo:
            resultado.append(num)
    return resultado

L = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
min = 3

print(filtrar_frequencias(L, 3))