import re

texto = input("Digite um texto: ")

emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    texto
)

telefones = re.findall(
    r'\(\d{2}\)\d{4,5}-\d{4}',
    texto
)

texto_limpo = re.sub(r'\s+', ' ', texto).strip()

print("\nE-mails encontrados:")
for email in emails:
    print(email)

print("\nTelefones encontrados:")
for telefone in telefones:
    print(telefone)

print("\nTexto limpo:")
print(texto_limpo)