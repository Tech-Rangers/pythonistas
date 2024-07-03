from typing import TypedDict

class PetDict(TypedDict):
    nome: str
    especie: str
    peso: float
    idade: float
    dono: str



animais = [
    PetDict({'nome': 'Murphy', 'especie':'Gato', 'idade': 6, 'peso': 5.5, 'dono': 'Juliana'}),
    PetDict(nome='Bernardo', especie='Cão', idade=6, peso=10, dono='Marcela'),
    PetDict(nome='Anabele', especie='Peixe', idade=6, peso=1, dono='Marcela'),
    PetDict(nome='Hórus', especie='Gato', idade=2, peso=10, dono='Leiticia'),
    PetDict(nome='Pipoca', especie='Peixe', idade=6, peso=10, dono='Juliana'),
    PetDict(nome='Kronos', especie='Tartaruga', idade=4, peso=3, dono='Carlos'),
    PetDict(nome='Poseidon', especie='Cão', idade=4, peso=5, dono='Gabriel'),
    PetDict(nome='Fumaça', especie='Gato', idade=2, peso=4, dono='Juliana'),
    PetDict(nome='Zeus', especie='Gato', idade=6, peso=9.0, dono='Gabriel'),
    PetDict(nome='Koda', especie='Cão', idade=6, peso=19.0, dono='Carlos'),
    PetDict(nome='Fumaça', especie='Hamster', idade=1, peso=0.5, dono='Savanna'),
    PetDict(nome='Hórus', especie='Calopsita', idade=7, peso=0.1, dono='Carlos'),
]

color_green = "\33[32m"
color_yellow= "\33[33m"
color_red= "\33[31m"
color_blue= "\33[36m"
style = "\33[1m"


# 1
def adicionar_animal():
    nome_pet = str(input('Qual o nome do seu pet? '))
    espécie = str(input('Qual a espécie do seu pet? '))
    idade = int(input('Qual idade do seu pet? '))
    peso = str(input('Qual o peso do seu pet(em kg)? '))
    nome_dono = str(input('Qual é o seu nome(nome do dono)? '))
    pet = PetDict(nome=nome_pet.capitalize(), dono=nome_dono, especie=espécie, idade=idade, peso=peso)
    print(f'{color_green}O novo animal cadastrado é: \033[0m {pet} \n')
    animais.append(pet)


# 2
def remover_animal():
    nome_pet = str(input('Qual o nome do seu pet a ser removido? '))
    for index, animal in enumerate(animais):
        if nome_pet == animal['nome']:
            print(f'{color_red} O animal a ser removido é:  \033[0m {animal}')
            animais.remove(animal)
            return

    print("Não tem o nome pet")

# 3
def exibir_todos_os_animais():
    align = "^"
    width = 48
    fill="="
    message0=" Todos animais em ordem "
    print(f"| {message0:{fill}{align}{width}} |")

    # headers
    width = 10
    message1 = 'Nome Pet'
    message2 = 'Espécie'
    message3 = 'Idade'
    message4 = 'Peso(kg)'
    message5 = 'Dono'
    print(f'|{message1:{align}{width}}{message2:{align}{width}}{message3:{align}{width}}{message4:{align}{width}}{message5:{align}{width}}|')

    animais_em_ordem = []
    letras_alfabeto = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "X", "Z"]

    for letra in letras_alfabeto:
        for animal in animais:
            if letra in animal['nome'][0]:
                if animal not in animais_em_ordem:
                    animais_em_ordem.append(animal)
                    print(f'|{animal["nome"]:{align}{width}}{animal['especie']:{align}{width}}{animal['idade']:{align}{width}}{animal["peso"]:{align}{width}}{animal['dono']:{align}{width}}|')


    print("Todos animais FORA DE ordem")



    for animal in animais:
        print(f'|{animal["nome"]:{align}{width}}{animal['especie']:{align}{width}}{animal['idade']:{align}{width}}{animal["peso"]:{align}{width}}{animal['dono']:{align}{width}}|')
    print('\n\n')

# 4
def buscar_animal_pelo_nome():
    nome_pet = input(" => Qual o nome do animal que deseja procurar?  ")
    for animal in animais:
        if nome_pet == animal['nome']:
            print(f"{color_yellow} O pet {nome_pet} possui os dados:\033[0m  {animal}\n")
            return

    print("Não encontramos este pet \n")


# 5
def buscar_animais_do_dono():
    nome_dono = input(" => Qual o nome do dono que deseja procurar os animais?  ")

    animais_encontrados = []
    for index, animal in enumerate(animais):
        if  nome_dono in animal['dono']:
            animais_encontrados.append(animal)

    if animais_encontrados:
        for animal in animais_encontrados:
            print(f'{color_yellow} A pessoa: \033[0m {nome_dono} {color_yellow} é dono de: \033[0m {animal}')
    else:
        print('Não há animais cadastrados desta pessoa\n')

# 6
def atualizar_animal():
    nome_pet = input(" => Qual o nome do animal que deseja atualizar?  ")
    encontrou_algum_animal = False
    pet_atualizado = None

    for animal in animais:
        if nome_pet in animal['nome']:
            encontrou_algum_animal = True
            resposta = input(f'O animal é: {animal}, este é o animal que gostaria de atualizar? (Sim ou Não): ')

            if resposta in ["Sim", "sim", "SIM", "S", "s"]:
                nova_especie = str(input('Qual a espécie do seu pet?'))
                nova_idade = int(input('Qual a idade do seu pet?'))
                novo_peso = float(input('Qual o peso do seu pet?'))

                pet_atualizado = PetDict(nome=animal['nome'], especie=nova_especie, idade=nova_idade, peso=novo_peso, dono=animal['dono'])

    if not encontrou_algum_animal:
        print('Não foi encontrado nenhum animal com este nome\n')
        return

    if pet_atualizado is None:
        print("Não foi possivel prosseguir com a atualização\n")
    else:
        print(f'{color_green}O animal atualizado é: \033[0m {pet_atualizado}')
        animais.append(pet_atualizado)
        animais.remove(animal)


def mostrar_menu():
    print('\n')
    print('-=- MENU -=-')
    print("1 - Adicionar Animal")
    print("2 - Removel Animal")
    print("3 - Exibir Todos os Animais")
    print("4 - Buscar Animal Pelo Nome")
    print("5 - Buscar Animais do Dono")
    print("6 - Atualizar Animal")
    print("0 - Sair")
    print('\n\n')

def sair():
    print("\nTchau 👋")
    exit(1)

def iniciar_loop_principal():
    print("-=- Bem vindo ao Petshop -=- ")
    mostrar_menu()

    comandos = {
        "0": sair,
        "1": adicionar_animal,
        "2": remover_animal,
        "3": exibir_todos_os_animais,
        "4": buscar_animal_pelo_nome,
        "5": buscar_animais_do_dono,
        "6": atualizar_animal,
    }

    user_input = None
    while True:
        try:
            user_input = input("Como posso ajudar?\n")

            if user_input not in comandos:
                print("Por favor digite uma opção valida!!!\n")
                continue

            comandos[user_input]()
        except (KeyboardInterrupt, EOFError):
            sair()
        except (KeyError):
            print("Comando não reconhecido. Digite 'help' ou 'ajuda' para listar as ações disponíveis")


if __name__ == "__main__":
    iniciar_loop_principal()
