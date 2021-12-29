from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida
from fabrica_fila import FabricaFila

fila_teste = FabricaFila.pega_fila(TIPO_FILA_NORMAL)
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(10))

fila_prioritaria = FabricaFila.pega_fila(TIPO_FILA_PRIORITARIA)
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
print(fila_prioritaria.chama_cliente(5))
print(fila_prioritaria.chama_cliente(10))
print(fila_prioritaria.estatistica('20/03/2020', 120, EstatisticaDetalhada))
print(fila_prioritaria.estatistica('20/03/2020', 120, EstatisticaResumida))
