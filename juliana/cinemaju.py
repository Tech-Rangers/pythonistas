from typing import TypedDict
import random
import copy

color_green = "\33[32m"
color_yellow= "\33[33m"
color_red= "\33[31m"
color_blue= "\33[36m"
style = "\33[1m"

print('\n')
print('-=- SEJAM BEM VIADOS AO CINEMA JU -=-')
print("-=-       Catálogo de filmes      -=-")
print("Planeta dos Macacos: O Reinado")
print("Divertidamente")
print("Garfield")
print("Furiosa")
print("Bad Boys")
print('\n\n')



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

compras_realizadas = []
saldo_final = 0
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
                compras_realizadas.append(pessoa)
                #print(f"As compras realizadas são: {compras_realizadas} para o filme {filme}")
                return
                            
def exibir_sala():
    
    print(f'{filme}\n')
    print(salas_passando_filme[0])
    print(salas_passando_filme[0])
    print(salas_passando_filme[0])
    print('\n')
    print(f"As pessoas que compraram foram: {compras_realizadas}\n")




def comprar_ingresso_casal(casal):
    print(f'Compra de ingresso casal: {casal}')
    for letra, fileira in enumerate(salas_passando_filme[filme]):
        for numero, assento in enumerate(fileira):
            if numero == len(fileira) - 1:
                continue
            
            assento_lado = fileira [numero + 1]
            
            if assento == 0 and assento_lado == 0:
                salas_passando_filme[filme][letra][numero] = 1
                salas_passando_filme[filme][letra][numero + 1] = 1
                print(f"Filme {filme} - Assentos comprados {converter_numero_do_assento(letra, numero)} e {converter_numero_do_assento(letra, numero + 1)} ")
                compras_realizadas.append(casal)
                #print(f"As compras realizadas são: {compras_realizadas} para o filme {filme}")
                return
    print(f"Não foi possivel realizar esta compra para o filme: {filme}")

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



