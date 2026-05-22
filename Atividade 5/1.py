import os
from datetime import datetime

caminho = input("Digite o caminho da pasta: ")

total_arquivos = 0
total_pastas = 0
tamanho_total = 0

if os.path.exists(caminho):

    itens = os.listdir(caminho)

    for item in itens:
        caminho_completo = os.path.join(caminho, item)

        if os.path.isfile(caminho_completo):
            total_arquivos += 1

            tamanho = os.path.getsize(caminho_completo)
            tamanho_total += tamanho

            timestamp = os.path.getmtime(caminho_completo)
            data_modificacao = datetime.fromtimestamp(timestamp)

            print(f"Arquivo: {item}")
            print(f"Tamanho: {tamanho} bytes")
            print(f"Última modificação: {data_modificacao}")
            print("-" * 40)

        elif os.path.isdir(caminho_completo):
            total_pastas += 1
            print(f"Pasta: {item}")

    print("\nResumo:")
    print(f"Total de arquivos: {total_arquivos}")
    print(f"Total de pastas: {total_pastas}")
    print(f"Tamanho total dos arquivos: {tamanho_total} bytes")

else:
    print("Caminho inválido!")