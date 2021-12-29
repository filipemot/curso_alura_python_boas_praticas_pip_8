# PEP 8  (https://www.python.org/dev/peps/pep-0008/)
from typing import Dict, Union, List, Tuple, Set

from constantes import CODIGO_NORMAL
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
from fila_base import FilaBase

Classes = Union[EstatisticaDetalhada, EstatisticaResumida]

class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'${CODIGO_NORMAL}{str(self.codigo)}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatistica(self, retorna_estatistica: Classes) -> dict:
        return retorna_estatistica.roda_estatistica(self.cliente_atendidos)
