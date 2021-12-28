# Fora da PEP 8 (https://www.python.org/dev/peps/pep-0008/)
from constantes import CODIGO_PRIORITARIO
from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'${CODIGO_PRIORITARIO}{str(self.codigo)}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}"
