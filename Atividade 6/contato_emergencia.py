from contato import Contato


class ContatoEmergencia(Contato):
    __slots__ = ("_prioridade",)

    def __init__(self, nome, telefone,
                 datanasc, email, prioridade=True):

        super().__init__(
            nome,
            telefone,
            datanasc,
            email
        )

        self._prioridade = prioridade

    @property
    def prioridade(self):
        return self._prioridade

    def __str__(self):
        return (
            super().__str__() +
            f"\nPrioridade: {self.prioridade}"
        )