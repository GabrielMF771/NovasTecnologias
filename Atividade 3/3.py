def existe_subconjunto(lista, n, alvo):
    if alvo == 0:
        return True
    if n == 0:
        return False
    if lista[n-1] > alvo:
        return existe_subconjunto(lista, n-1, alvo)
    
    return existe_subconjunto(lista, n-1, alvo) or \
        existe_subconjunto(lista, n-1, alvo - lista[n-1])

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

if (existe_subconjunto(L, len(L), target)):
    print(f"Encontrado subconjunto com soma {target}")
else:
    print("Não encontrado!")
