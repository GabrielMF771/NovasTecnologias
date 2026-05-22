import os
import zipfile

diretorio = os.path.dirname(__file__)

nome_zip = os.path.join(diretorio, "backup.zip")

arquivos_txt = []

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".txt"):
        arquivos_txt.append(arquivo)

with zipfile.ZipFile(nome_zip, "w", zipfile.ZIP_DEFLATED) as zipf:

    for arquivo in arquivos_txt:
        caminho_arquivo = os.path.join(diretorio, arquivo)

        zipf.write(caminho_arquivo, arcname=arquivo)

print("Arquivos adicionados ao backup:\n")

with zipfile.ZipFile(nome_zip, "r") as zipf:

    for arquivo in arquivos_txt:
        caminho_arquivo = os.path.join(diretorio, arquivo)

        tamanho_original = os.path.getsize(caminho_arquivo)

        info = zipf.getinfo(arquivo)
        tamanho_comprimido = info.compress_size

        print(f"Arquivo: {arquivo}")
        print(f"Tamanho original: {tamanho_original} bytes")
        print(f"Tamanho comprimido: {tamanho_comprimido} bytes")
        print("-" * 40)