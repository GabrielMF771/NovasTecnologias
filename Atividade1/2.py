numero_str = input("Digite um número: ")

base = int(input("Digite a base: "))

numero_int = int(numero_str, base)

print("Valor em decimal: ", numero_int)
print("Valor em hexadecimal: ", hex(numero_int))
print("Valor em octal: ", oct(numero_int))