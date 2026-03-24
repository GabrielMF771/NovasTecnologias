def sao_anagramas(texto1, texto2):
    return sorted(texto1) == sorted(texto2)

print("Verificação de Anagrama!")
texto1 = input("Digite o primeiro texto:\n")
texto2 = input("Digite o segundo texto:\n")

if(sao_anagramas(texto1, texto2)):
    print("São anagramas!")
else:
    print("Não são anagramas")