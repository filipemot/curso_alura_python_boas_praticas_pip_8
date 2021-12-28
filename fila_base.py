import abc
from typing import List

from constantes import TAMANHO_PADRAO_MINIMO, TAMANHO_PADRAO_MAXIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    cliente_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def insere_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()