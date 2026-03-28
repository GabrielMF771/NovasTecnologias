def mesclar_intervalos(intervalos):
    if not intervalos:
        return []
    
    intervalos_ordenados = sorted(intervalos, key=lambda x: x[0])

    mesclados = [intervalos_ordenados[0]]

    for atual in intervalos_ordenados[1:]:
        ultimo_inicio, ultimo_fim = mesclados[-1]
        inicio_atual, fim_atual = atual
        if inicio_atual <= ultimo_fim:
            mesclados[-1] = (ultimo_inicio, max(ultimo_fim, fim_atual))
        else:
            mesclados.append(atual)
    return mesclados
    
entrada = [(1, 4), (2, 5), (7, 9)]
resultado = mesclar_intervalos(entrada)
print(f"Intervalos originais: {entrada}")
print(f"Intervalos mesclados: {resultado}")
