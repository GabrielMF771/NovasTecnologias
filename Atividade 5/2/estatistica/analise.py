def estatisticas(dados, campo):
    valores = []

    # Pega apenas os valores numéricos
    for linha in dados:
        if campo in linha and isinstance(linha[campo], (int, float)):
            valores.append(linha[campo])

    # Verifica se encontrou valores
    if len(valores) == 0:
        return {
            "erro": f"Campo '{campo}' não encontrado ou não numérico"
        }

    resultado = {
        "media": sum(valores) / len(valores),
        "minimo": min(valores),
        "maximo": max(valores),
        "total": sum(valores)
    }

    return resultado