from typing import List, Union, Dict


class EstatisticaResumida:

    def __init__(self, dia: str, agencia: str):
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, cliente_atendidos: List[str]) -> dict:
        statistic: Dict[str, Union[List[str], str, int]] = {
            f'{self.agencia} - {self.dia}': len(cliente_atendidos)}

        return statistic
