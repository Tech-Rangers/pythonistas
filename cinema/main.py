import random

import copy

pessoas = [
    "Ana",              # solteira -> type("Ana") == str
    ["Bruno", "Carla"], # casal    -> type(["Bruno", "Carla"]) == list
    "Daniel",
    ["Eduardo", "Fernanda"],
    "Gabriela",
    "Helena",
    ["Igor", "Juliana"],
    "Lucas",
    ["Mariana", "Nicolas"],
    "Olivia",
    "Pedro",
    ["Quentin", "Rafaela"],
    "Sofia",
    ["Thiago", "Ursula"],
    "Vanessa",
    "William",
    ["Xavier", "Yara"],
    "Zoe",
    ["Arthur", "Beatriz"],
    "Camila",
    ["Davi", "Elena"],
    "Felipe",
    ["Gustavo", "Heloisa"],
    "Isabel",
    ["João", "Karina"],
    "Lara",
    ["Miguel", "Natália"],
    "Otávio",
    ["Paulo", "Renata"]
]

filmes = [
    "Planeta dos Macacos: O Reinado",
    "Divertidamente 2",
    "Garfield",
    "Furiosa",
    "Bad Boys",
]


sala_vazia = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


# Funções Auxiliares/ debug
def print_salas(salas):
    salas["Bad Boys"][0][0] = 1
    print(" === salas passando filme === ")
    for sala in salas:
        print(sala, salas[sala])

    print('\n\n')

def converter_numero_do_assento(i, j):
    fileiras = ["A", "B", "C"]
    numeros_do_assento = ["1","2","3"]
    return fileiras[i] + numeros_do_assento[j]

# Funções principais

def escolher_filme():
    return random.choice(filmes)

def comprar_ingresso_solo(pessoa, filme):
    print(f'Compra de ingresso solo: {pessoa}')
    for letra, fileira in enumerate(salas_passando_filme[filme]):
        for numero, assento in enumerate(fileira):
            if assento == 0:
                salas_passando_filme[filme][letra][numero] = 1
                print(f"Filme {filme} - Assento comprado {converter_numero_do_assento(letra, numero)} ")
                return


def comprar_ingresso_casal(casal):
    print(f'Compra de ingresso casal: {casal}')


# INICIO DO PROGRAMA


salas_passando_filme = {}

for filme in filmes:
    salas_passando_filme[filme] = copy.deepcopy(sala_vazia)

print(" === compra de ingresso === ")
for p in pessoas:
    filme_escolhido = escolher_filme()
    if type(p) == str:
        comprar_ingresso_solo(pessoa=p, filme=filme_escolhido)
    if type(p) == list:
        comprar_ingresso_casal(p)

print_salas(salas_passando_filme)