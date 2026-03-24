a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
p = int(input("Digite o valor de p (passo): "))

if p == 0:
    print("Erro: o passo não pode ser zero.")
elif a < b and p <= 0:
    print("Erro: se a < b, o passo deve ser positivo.")
elif a > b and p >= 0:
    print("Erro: se a > b, o passo deve ser negativo.")
else:
    print(f"Valores de {a} a {b}: ") 
    valores = list(range(a, b + (1 if p > 0 else -1), p))

    print("Valores gerados:")
    for v in valores:
        print(v)
        
    print(f"Foram impressos {len(valores)} valores.")