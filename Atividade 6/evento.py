from datetime import date
from contato import Contato


class Evento:
    _total_eventos = 0

    def __init__(self,
                 descricao: str,
                 data_inicio: date,
                 data_fim: date,
                 contato: Contato):

        self._descricao = descricao
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._contato = contato

        Evento._total_eventos += 1

    def get_informacoes(self) -> str:
        return (
            f"Descrição: {self._descricao}\n"
            f"Data início: "
            f"{self._data_inicio.strftime('%d/%m/%Y')}\n"
            f"Data fim: "
            f"{self._data_fim.strftime('%d/%m/%Y')}\n"
            f"Contato: {self._contato.nome}"
        )

    @staticmethod
    def get_total_eventos() -> int:
        return Evento._total_eventos