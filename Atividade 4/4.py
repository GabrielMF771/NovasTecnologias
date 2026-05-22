import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def resto(a, b):
    return a % b

def potencia(a, b):
    return a ** b

def raiz(a):
    return math.sqrt(a)

def fatorial(a):
    return math.factorial(a)

def logaritmo(a):
    return math.log(a)

def cosseno(a):
    return math.cos(a)

def seno(a):
    return math.sin(a)

def tangente(a):
    return math.tan(a)


def aplicar_operacao(operacao, a=None, b=None):
    if b is not None:
        return operacao(a, b)
    return operacao(a)


print("Soma:", aplicar_operacao(soma, 10, 5))
print("Subtração:", aplicar_operacao(subtracao, 10, 5))
print("Multiplicação:", aplicar_operacao(multiplicacao, 10, 5))
print("Divisão:", aplicar_operacao(divisao, 10, 5))
print("Resto:", aplicar_operacao(resto, 10, 3))
print("Potência:", aplicar_operacao(potencia, 2, 3))

print("Raiz:", aplicar_operacao(raiz, 25))
print("Fatorial:", aplicar_operacao(fatorial, 5))
print("Logaritmo:", aplicar_operacao(logaritmo, 10))
print("Cosseno:", aplicar_operacao(cosseno, 0))
print("Seno:", aplicar_operacao(seno, math.pi / 2))
print("Tangente:", aplicar_operacao(tangente, 1))