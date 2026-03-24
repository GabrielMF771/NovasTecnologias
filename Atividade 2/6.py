print("Sistema de Atendimento")
print("""
A - Abrir atendimento
T - Triagem
E - Encaminhar
F - Finalizar
S - Sair
""")
estado = "inicial"

while True:
    comando = input("Digite a opção desejada: ").upper()
    match comando:
        case "A":
            if estado == "inicial":
                estado = "aberto"
                print("Atendimento aberto.")
            else:
                print("Erro: só é possível abrir quando está no estado inicial.")
        case "T":
            if estado == "aberto":
                estado = "triado"
                print("Triagem realizada.")
            else:
                print("Erro: só é possível triagem se estiver aberto.")
        case "E":
            if estado == "triado":
                estado = "encaminhado"
                print("Atendimento encaminhado.")
            else:
                print("Erro: só é possível encaminhar se estiver triado.")
        case "F":
            if estado == "encaminhado":
                estado = "finalizado"
                print("Atendimento finalizado.")
            else:
                print("Erro: só é possível finalizar se estiver encaminhado.")
        case "S":
            print("Saindo do sistema...")
            break
        case _:
            print("Comando inválido.")      
