from typing import List, Union, Dict


class EstatisticaDetalhada:

    def __init__(self, dia: str, agencia: str):
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, cliente_atendidos: List[str]) -> dict:
        statistic: Dict[str, Union[List[str], str, int]] = {'dia': self.dia, 'agencia': self.agencia,
                                                            'clientes_atendidos': cliente_atendidos,
                                                            'quantidade_clientes_atendidos': len(cliente_atendidos)}

        return statistic
