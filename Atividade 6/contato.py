from datetime import date


class Contato:
    __slots__ = ("_nome", "_telefone", "_datanasc", "_email")

    def __init__(self, nome: str, telefone: str,
                 datanasc: date, email: str):
        self.nome = nome
        self.telefone = telefone
        self.datanasc = datanasc
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @property
    def datanasc(self):
        return self._datanasc

    @datanasc.setter
    def datanasc(self, valor):
        if isinstance(valor, date):
            self._datanasc = valor
        else:
            raise ValueError(
                "A data de nascimento deve ser do tipo datetime.date"
            )

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"Data de nascimento: "
            f"{self.datanasc.strftime('%d/%m/%Y')}\n"
            f"E-mail: {self.email}"
        )