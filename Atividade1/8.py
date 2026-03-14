def criptografar(numero):
    digitos = [int(d) for d in str(numero).zfill(4)]
    
    digitos = [(d + 7) % 10 for d in digitos]
    
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]
    
    return "".join(str(d) for d in digitos)


def descriptografar(numero):
    digitos = [int(d) for d in str(numero).zfill(4)]
    
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]
    
    digitos = [(d - 7) % 10 for d in digitos]
    
    return "".join(str(d) for d in digitos)


numero = input("Digite um número de 4 dígitos: ")
criptografado = criptografar(numero)
print("Número criptografado:", criptografado)

numero_cripto = input("Digite o número criptografado: ")
original = descriptografar(numero_cripto)
print("Número original:", original)
