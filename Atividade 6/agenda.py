from contato import Contato
from evento import Evento


class Agenda:
    _contatos = []
    _eventos = []

    def __init__(self, item=None):

        if isinstance(item, Contato):
            Agenda._contatos.append(item)

        elif isinstance(item, Evento):
            Agenda._eventos.append(item)

    @staticmethod
    def contatos():
        return Agenda._contatos

    @staticmethod
    def eventos():
        return Agenda._eventos