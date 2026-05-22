import csv


def converter_valor(valor):
    try:
        return int(valor)
    except ValueError:
        pass

    try:
        return float(valor)
    except ValueError:
        pass

    return valor


def ler_csv(caminho):
    dados = []

    with open(caminho, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha_convertida = {}

            for chave, valor in linha.items():
                linha_convertida[chave] = converter_valor(valor)

            dados.append(linha_convertida)

    return dados