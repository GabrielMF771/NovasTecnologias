from datetime import datetime
from contato import Contato
from contato_emergencia import ContatoEmergencia
from evento import Evento
from agenda import Agenda


def ler_data(mensagem):
    while True:
        try:
            data_str = input(mensagem)
            return datetime.strptime(
                data_str,
                "%d/%m/%Y"
            ).date()

        except ValueError:
            print(
                "Data inválida! "
                "Use o formato DD/MM/AAAA."
            )


def criar_contato(emergencia=False):
    try:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        data = ler_data(
            "Data de nascimento (DD/MM/AAAA): "
        )
        email = input("Email: ")

        if emergencia:
            contato = ContatoEmergencia(
                nome,
                telefone,
                data,
                email
            )
        else:
            contato = Contato(
                nome,
                telefone,
                data,
                email
            )

        Agenda(contato)

        print(
            "\nContato cadastrado "
            "com sucesso!\n"
        )

    except Exception as e:
        print(f"Erro: {e}")


def listar_contatos():
    contatos = Agenda.contatos()

    if not contatos:
        print("\nNenhum contato cadastrado.\n")
        return

    print("\n===== CONTATOS =====")

    for i, contato in enumerate(
        contatos, start=1
    ):
        print(f"\nContato {i}")
        print(contato)


def editar_contato():
    contatos = Agenda.contatos()

    if not contatos:
        print(
            "\nNenhum contato "
            "para editar.\n"
        )
        return

    listar_contatos()

    try:
        indice = int(
            input(
                "\nDigite o número "
                "do contato: "
            )
        ) - 1

        contato = contatos[indice]

        contato.nome = input(
            "Novo nome: "
        )

        contato.telefone = input(
            "Novo telefone: "
        )

        contato.datanasc = ler_data(
            "Nova data "
            "(DD/MM/AAAA): "
        )

        contato.email = input(
            "Novo email: "
        )

        print(
            "\nContato editado "
            "com sucesso!\n"
        )

    except (
        IndexError,
        ValueError
    ):
        print("Contato inválido!")


def criar_evento():
    contatos = Agenda.contatos()

    if not contatos:
        print(
            "\nCadastre um contato "
            "antes do evento.\n"
        )
        return

    try:
        descricao = input(
            "Descrição do evento: "
        )

        data_inicio = ler_data(
            "Data de início "
            "(DD/MM/AAAA): "
        )

        data_fim = ler_data(
            "Data de fim "
            "(DD/MM/AAAA): "
        )

        print(
            "\nEscolha um contato:"
        )

        for i, contato in enumerate(
            contatos, start=1
        ):
            print(
                f"{i} - "
                f"{contato.nome}"
            )

        indice = int(
            input("Número: ")
        ) - 1

        contato_escolhido = contatos[indice]

        evento = Evento(
            descricao,
            data_inicio,
            data_fim,
            contato_escolhido
        )

        Agenda(evento)

        print(
            "\nEvento criado "
            "com sucesso!\n"
        )

    except (
        ValueError,
        IndexError
    ):
        print("Erro ao criar evento!")


def listar_eventos():
    eventos = Agenda.eventos()

    if not eventos:
        print(
            "\nNenhum evento "
            "cadastrado.\n"
        )
        return

    print("\n===== EVENTOS =====")

    for i, evento in enumerate(
        eventos, start=1
    ):
        print(f"\nEvento {i}")
        print(
            evento.get_informacoes()
        )


while True:
    print("\n===== AGENDA =====")
    print("1 - Criar contato")
    print("2 - Editar contato")
    print("3 - Listar contatos")
    print(
        "4 - Criar contato "
        "de emergência"
    )
    print("5 - Criar evento")
    print("6 - Listar eventos")
    print("7 - Sair")

    try:
        opcao = int(
            input(
                "Escolha uma opção: "
            )
        )

        match opcao:
            case 1:
                criar_contato()

            case 2:
                editar_contato()

            case 3:
                listar_contatos()

            case 4:
                criar_contato(
                    emergencia=True
                )

            case 5:
                criar_evento()

            case 6:
                listar_eventos()

            case 7:
                print(
                    f"\nTotal de "
                    f"eventos: "
                    f"{Evento.get_total_eventos()}"
                )

                print("Saindo...")
                break

            case _:
                print(
                    "Opção inválida!"
                )

    except ValueError:
        print(
            "Digite um número válido!"
        )