eventos = {}


def registrar_evento(resultado, funcao):
    eventos[resultado] = funcao


def disparar_evento(resultado):
    if resultado in eventos:
        eventos[resultado]()
    else:
        print("Nenhum evento aconteceu.")