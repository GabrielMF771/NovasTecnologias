def multiplicar_polinomios(p1, p2):
    resultado = {}

    for exp1, coef1 in p1.items():
        for exp2, coef2 in p2.items():
            novo_exp = exp1 + exp2
            
            novo_coef = coef1 * coef2
            
            if novo_exp in resultado:
                resultado[novo_exp] += novo_coef
            else:
                resultado[novo_exp] = novo_coef

    return resultado


p1 = {2: 3, 1: 2, 0: 1} # 3x² + 2x + 1
p2 = {1: 4, 0: 5} # 4x + 5

resultado = multiplicar_polinomios(p1, p2)

print(resultado)