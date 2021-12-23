#Fora da PEP 8 (https://www.python.org/dev/peps/pep-0008/)
from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gerasenhaatual(self) -> None:
        self.senha_atual = str(self.codigo)

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gerasenhaatual()
        self.fila.append(f"NM{self.senha_atual}")

    def chamacliente(self, caixa: int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}"