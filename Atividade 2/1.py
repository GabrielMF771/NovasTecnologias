import re
def eh_palindromo(texto):
    texto_limpo = re.sub(r'[^a-zA-Z]', '', texto)

    texto_limpo = texto_limpo.lower()

    return texto_limpo == texto_limpo[::-1]

resposta = input("Digite uma palavra para verificar se é palíndromo ou não:\n")
print("")

if(eh_palindromo(resposta)):
    print(f"{resposta} é um palíndromo!")
else:
    print(f"{resposta} não é um palíndromo...")
