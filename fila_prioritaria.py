# PEP 8  (https://www.python.org/dev/peps/pep-0008/)
from constantes import CODIGO_NORMAL
from fila_base import FilaBase


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'${CODIGO_NORMAL}{str(self.codigo)}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}: {self.cliente_atendidos}'}
        else:
            estatistica = {'dia': dia, 'agencia': (agencia,), 'cliente_atendidos': self.cliente_atendidos,
                           'quantidade_cliente_atendidos': len(self.cliente_atendidos)}

        return estatistica
