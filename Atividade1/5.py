texto = input("Digite um texto com o formato: YYYY-MM-DD HH:MM:SS - mensagem: ")

print("Data: " + texto[:9])
print("Hora: " + texto[11:19])
print("Mensagem: " + texto [20:])