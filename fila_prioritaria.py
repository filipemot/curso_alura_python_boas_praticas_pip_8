# PEP 8  (https://www.python.org/dev/peps/pep-0008/)
class FilaPrioritaria:
    codigo: int = 0
    fila = []
    cliente_atendidos = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        self.senha_atual = str(self.codigo)

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(f'PR{self.senhaatual}')

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia} - {dia}: {self.cliente_atendidos}'}
        else:
            estatistica = {'dia': dia, 'agencia': agencia, 'cliente_atendidos': self.cliente_atendidos,
                           'quantidade_cliente_atendidos': len(self.cliente_atendidos)}

        return estatistica
