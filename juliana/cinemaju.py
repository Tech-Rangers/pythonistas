from typing import TypedDict
import random

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
    ["Ana", "0"],              # solteira -> type("Ana") == str
    ["Bruno", "Carla"], # casal    -> type(["Bruno", "Carla"]) == list
    ["Daniel",  "0"],
    ["Eduardo", "Fernanda"],
    ["Gabriela","0"],
    ["Helena","0"],
    ["Igor", "Juliana"],
    ["Lucas","0"],
    ["Mariana", "Nicolas"],
    ["Olivia","0"],
    ["Pedro","0"],
    ["Quentin", "Rafaela"],
    ["Sofia","0"],
    ["Thiago", "Ursula"],
    ["Vanessa","0"],
    ["William","0"],
    ["Xavier", "Yara"],
    ["Zoe","0"],
    ["Arthur", "Beatriz"],
    ["Camila","0"],
]

    

sala_planeta_macacos = [
    {'A1': 0, 'A2': 0, 'A3': 0},
    {'B1': 0, 'B2': 0, 'B3': 0},
    {'C1': 0, 'C2': 0, 'C3': 0},
]
sala_divertidamente = [
    {'A1': 0, 'A2': 0, 'A3': 0},
    {'B1': 0, 'B2': 0, 'B3': 0},
    {'C1': 0, 'C2': 0, 'C3': 0},
]
sala_garfield = [
    {'A1': 0, 'A2': 0, 'A3': 0},
    {'B1': 0, 'B2': 0, 'B3': 0},
    {'C1': 0, 'C2': 0, 'C3': 0},
]
sala_furiosa = [
    {'A1': 0, 'A2': 0, 'A3': 0},
    {'B1': 0, 'B2': 0, 'B3': 0},
    {'C1': 0, 'C2': 0, 'C3': 0},
]
sala_badboys = [
    {'A1': 0, 'A2': 0, 'A3': 0},
    {'B1': 0, 'B2': 0, 'B3': 0},
    {'C1': 0, 'C2': 0, 'C3': 0},
]

class filmdict(TypedDict):
    nome_filme: str
    sala_filme: str

filmes = [
    filmdict(nome_filme = 'Planeta dos Macacos: O Reinado', sala_filme = sala_planeta_macacos),
    filmdict(nome_filme = 'Divertidamente', sala_filme = sala_divertidamente),
    filmdict(nome_filme = "Garfield", sala_filme = sala_garfield),
    filmdict(nome_filme = "Furiosa", sala_filme = sala_furiosa),
    filmdict(nome_filme = "Bad Boys", sala_filme = sala_badboys)
]



def comprar_ingressos():
    saldo = 0
    compras_realizadas = []
    for pessoa in pessoas:
        filme_escolhido = filmes [random.randrange(len(filmes))]
        sala_filme = filme_escolhido['sala_filme']
        if pessoa[1] == "0":
            print(f"A pessoa {pessoa[0]} escolheu o filme {filme_escolhido['nome_filme']}")
            saldo = saldo + 10
            compras_realizadas.append(pessoa[0])
        else:
            print(f"As pessoas {pessoa[0]} e {pessoa[1]} escolheram o filme {filme_escolhido['nome_filme']}")
            compras_realizadas.append(pessoa)
            saldo = saldo + 20
    print('\n')
    print(sala_filme[0])
    print(sala_filme[1])
    print(sala_filme[2])
    print('\n')
    print(f"As pessoas que compraram hoje de hoje foram: {compras_realizadas}\n")
    total_compras = saldo / 10
    print(f"O total de compras de hoje foram: {total_compras}\n")   
    print(f" {color_green} Saldo final do cinema é de R$ {saldo:.2f}\033[0m")



def escolher_acentos_individual():
    for pessoa in pessoas:
        if pessoa[1] == '0':
            filme_escolhido = filmes [random.randrange(len(filmes))]
            sala_filme = filme_escolhido['sala_filme']
            print(f"A pessoa {pessoa[0]} escolheu o filme: {filme_escolhido['nome_filme']}")
            print('Painel de disponibilidade da sala: \n')
            print(sala_filme[0])
            print(sala_filme[1])
            print(sala_filme[2])
            print('\n')
            

            for lugar in range(len(sala_filme)):
                    print(lugar)
                    
                    fileira = sala_filme [random.randrange(len(sala_filme[lugar]))]
                    print(fileira)

                    if lugar in fileira:
                        print(f"O lugar escolhido pela {pessoa[0]} foi {lugar}")
                        lugar = 1
                        print(lugar)
                    
        else: 
            print(f"A pessoa {pessoa} precisa de 2 lugares")
    print('Painel de disponibilidade da sala: \n')
    print(sala_filme[0])
    print(sala_filme[1])
    print(sala_filme[2])
escolher_acentos_individual()

#def escolher_acentos_casal(): 


#def exibir_acentos():