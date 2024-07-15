""" 1. __main__ não pode ser importado por outro módulo. Este arquivo é sempre destinado a um script executável
    2. __main__ é o script executável do pacote que ele se encontra, no nosso caso, `python carlos/cinema` executa o __main__.py
"""

from dados import filmes, sala_vazia, pessoas
from funcoes import escolher_filme, comprar_ingresso_casal, comprar_ingresso_solo, print_salas

import copy

salas_passando_filme = {}

for filme in filmes:
    salas_passando_filme[filme] = copy.deepcopy(sala_vazia)

print(" === compra de ingresso === ")
for p in pessoas:
    filme_escolhido = escolher_filme(filmes)
    if type(p) == str:
        comprar_ingresso_solo(salas_passando_filme=salas_passando_filme, pessoa=p, filme=filme_escolhido)
    if type(p) == list:
        comprar_ingresso_casal(salas_passando_filme=salas_passando_filme, casal=p, filme=filme_escolhido)

print_salas(salas_passando_filme)