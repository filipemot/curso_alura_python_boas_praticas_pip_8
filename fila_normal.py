#Fora da PEP 8 (https://www.python.org/dev/peps/pep-0008/)
class fila_normal:
    codigo: int = 0
    fila = []
    clienteatendidos = []
    senhaatual:str = ""

    def gerasenhaatual(self) -> None:
        self.senhaatual = str(self.codigo)

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(f"NM{self.senhaatual}")

    def chamacliente(self, caixa: int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clienteatendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}"