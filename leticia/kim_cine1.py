from typing import TypedDict

class PetDict(TypedDict):
    pessoas: str
    lugar: str
    fileira: str
    filmes:str
    ingresso:str

pessoas = [
    "Ana",              
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

{
    "Planeta dos macacos:"[
        [ 
            [A1, A2, A3],
            [B1, B2, B3],
            [C1, C2, C3],
        ]
    ]
}

{
    "Divertidamente 2:"[
        [ 
            [A1, A2, A3],
            [B1, B2, B3],
            [C1, C2, C3],
        ]
    ]
}

{
    "Garfield:"[
        [ 
            [A1, A2, A3],
            [B1, B2, B3],
            [C1, C2, C3],
        ]
    ]
}
 
 {
    "Furiosa:"[
        [ 
            [A1, A2, A3],
            [B1, B2, B3],
            [C1, C2, C3],
        ]
    ]
}

{
    "Bad Boys:"[
        [ 
            [A1, A2, A3],
            [B1, B2, B3],
            [C1, C2, C3],
        ]
    ]
}

lugares=[
            ['A1', 'A2', 'A3'],
            ['B1', 'B2', 'B3'],
            ['C1', 'C2', 'C3'],
        ]

for lugares in fileiras:
    for lugares, pessoas in lugares_vagos.items():
        print(f"O lugardas {pessoas} é {nos lugares}")

for lugares in fileiras:
    for lugares, pessoas in lugares_comprados.items():
        print(f"O lugardas {pessoas} é nos{lugares_comprados}")

comprar_ingresso = []
for lugares in fileiras:
    if  'A1', 'A2', 'A3',
        'B1', 'B2', 'B3',
        'C1', 'C2', 'C3' in lugares:
        lugares_vagos.append(lugares) 

print(lugares_comprados) 
lugares_comprados = []
for lugares in fileiras:
    if  'A1', 'A2', 'A3',
        'B1', 'B2', 'B3',
        'C1', 'C2', 'C3' in lugares:
        lugares_comprados.append(lugares)
print(lugares_comprados)

lugares_vagos = []
for lugares in fileiras:
    if  'A1', 'A2', 'A3',
        'B1', 'B2', 'B3',
        'C1', 'C2', 'C3' in lugares:
        lugares_vagos.append(lugares)
print(lugares_vagos)

 def sortear_lugar(lugares: list[str]) -> str:
    return random.choice(lugares)

def quantidade_de_pessoas():
    pessoas = str(input('E um casal ou individual? '))
    pessoas = PetDict(pessoas=pessoas)
    print(f': \033[0m {pessoas} \n')
    pessoas.append(pessoas)

def quantidade_de_lugares_vagos():
    pessoas = str(input('lugares vagos '))
    lugares_vagos = PetDict(pessoas=lugares_vagos)
    print(f': \033[0m {lugares} \n')
    pessoas.append(lugares)

def quantidade_de_lugares_comprados():
    pessoas = str(input('lugares vagos '))
    lugares_vagos = PetDict(pessoas=lugares_comprados)
    print(f': \033[0m {lugares} \n')
    pessoas.append(lugares)

def iniciar_loop_principal():
    print("-=- Bem vindo ao cinema -=- ")
    mostrar_menu(filmes)

    user_input = None
    while True:
        try:
            user_input = input("Como posso ajudar?\n")

            if not user_input.isnumeric() or int(user_input) not in range(7):
                print("Por favor digite uma opção valida!!!\n")
                continue

            if int(user_input) == 0:
                qual o filme()
            if int(user_input) == 1:
                quantidade_de_pessoas()
            if int(user_input) == 2:
                quantidades_de_lugares_vagos()
            if int(user_input) == 3:
                quantidade_de_lugares_comprados()
        

        except (KeyboardInterrupt, EOFError):
            sair()
        except (KeyError):
            print("Comando não reconhecido. Digite 'help' ou 'ajuda' para listar as ações disponíveis")


if __name__ == "__main__":
    iniciar_loop_principal()