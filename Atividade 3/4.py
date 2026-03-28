L = "(( ) )"
pilha = []
deu_erro = False

for simbolo in L:
    if simbolo == "(":
        pilha.append(1)
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            deu_erro = True
            break

if not deu_erro and len(pilha) == 0:
    print("Sucesso: Todos os parênteses foram abertos e fechados corretamente!")
else:
    print("Erro: Os parênteses estão desbalanceados.")
