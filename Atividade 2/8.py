n = int(input("Digite um número inteiro maior que 0: "))

if n <= 0:
    print("Erro: o número deve ser maior que 0.")
else:
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        classificacao = "perfeito"
    elif soma > n:
        classificacao = "abundante"
    else:
        classificacao = "deficiente"
        
    print(f"Soma dos divisores próprios: {soma}")
    print(f"Classificação: {classificacao}")