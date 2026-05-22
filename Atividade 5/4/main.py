from jogo.dados import lancar_dado
from jogo.eventos import registrar_evento, disparar_evento


def sorte():
    print("Evento: Sorte! Você ganhou moedas!")


def azar():
    print("Evento: Azar! Você perdeu uma rodada!")


def bonus():
    print("Evento: Bônus! Jogue novamente!")


registrar_evento(6, sorte)
registrar_evento(1, azar)
registrar_evento(3, bonus)

resultado = lancar_dado()

print(f"Resultado do dado: {resultado}")

disparar_evento(resultado)