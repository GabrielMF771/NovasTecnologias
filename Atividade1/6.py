def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + deslocamento) % 26 + base)
            resultado += novo_char
        else:
            resultado += char
    return resultado

texto = input("Digite um texto: ")
deslocamento = int(input("Digite o deslocamento: "))

print("")


print("Resultado: " + cifra_cesar(texto, deslocamento))