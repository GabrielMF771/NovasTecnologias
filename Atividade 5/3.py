operadores = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

def avaliar(expressao):
    expressao = expressao.replace(" ", "")

    try:
        return int(expressao)
    except ValueError:
        try:
            return float(expressao)
        except ValueError:
            pass

    if expressao.startswith("("):
        nivel = 0
        parenteses_completos = True

        for i, char in enumerate(expressao):
            if char == "(":
                nivel += 1
            elif char == ")":
                nivel -= 1

            if nivel == 0 and i < len(expressao) - 1:
                parenteses_completos = False
                break

        if parenteses_completos:
            return avaliar(expressao[1:-1])

    nivel = 0

    for i in range(len(expressao) - 1, -1, -1):
        char = expressao[i]

        if char == ")":
            nivel += 1
        elif char == "(":
            nivel -= 1
        elif nivel == 0 and char in ['+', '-']:
            esquerda = avaliar(expressao[:i])
            direita = avaliar(expressao[i + 1:])

            return operadores[char](esquerda, direita)

    nivel = 0

    for i in range(len(expressao) - 1, -1, -1):
        char = expressao[i]

        if char == ")":
            nivel += 1
        elif char == "(":
            nivel -= 1
        elif nivel == 0 and char in ['*', '/']:
            esquerda = avaliar(expressao[:i])
            direita = avaliar(expressao[i + 1:])

            return operadores[char](esquerda, direita)

    raise ValueError("Expressão inválida")


expressoes = [
    "2 + 3",
    "10 - 4",
    "2 + 3 * 4",
    "(2 + 3) * 4",
    "10 / 2 + 3",
    "(10 - 2) * (3 + 1)"
]

print("Resultados:")

for expr in expressoes:
    print(f"{expr} = {avaliar(expr)}")