import unicodedata

palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

anagramas = {}

for palavra in palavras:
    chave = tuple(sorted(normalizar(palavra)))

    if chave not in anagramas:
        anagramas[chave] = []

    anagramas[chave].append(palavra)
    
for chave, grupo in anagramas.items():
    print(f"{chave}: {grupo}")