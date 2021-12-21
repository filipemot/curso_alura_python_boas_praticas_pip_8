from fila_normal import fila_normal
from fila_prioritaria import FilaPrioritaria

fila_teste = fila_normal()
fila_teste.atualizafila()
fila_teste.atualizafila()
fila_teste.atualizafila()
print(fila_teste.chamacliente(5))
print(fila_teste.chamacliente(10))

fila_prioritaria = FilaPrioritaria()
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
print(fila_prioritaria.chama_cliente(5))
print(fila_prioritaria.chama_cliente(10))
print(fila_prioritaria.estatistica("17/12/2021", 198, "detail"))
print(fila_prioritaria.estatistica("17/12/2021", 198, "not_detail"))
