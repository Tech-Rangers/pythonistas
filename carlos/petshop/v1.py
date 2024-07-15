animais = [
    ['Murphy', 'Gato', 6, 5.5, 'Juliana'],
    ['Bernardo', 'Cão', 6, '10', 'Marcela'],
    ['Anabele', 'Peixe', 6, '1', 'Marcela'],
    ['Hórus', 'Gato', 2, '10', 'Leiticia'],
    ['Pipoca', 'Peixe', 6, '10', 'Juliana'],
    ['Kronos', 'Tartaruga', 4, '3', 'Carlos'],
    ['Poseidon', 'Cão', 4, '5', 'Gabriel'],
    ['Fumaça', 'Gato', 2, '4', 'Juliana'],
    ['Zeus', 'Gato', 6, 9.0, 'Gabriel'],
    ['Koda', 'Cão', 6, 19.0, 'Carlos'],
    ['Fumaça', 'Hamster', 1, 0.5, 'Savanna'],
    ['Hórus', 'Calopsita', 7, 0.1, 'Carlos'],
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
    pet = [nome_pet, espécie, idade, peso, nome_dono]
    print(f'{color_green}O novo animal cadastrado é: \033[0m {pet} \n')
    animais.append(pet)


# 2
def remover_animal():
    nome_pet = str(input('Qual o nome do seu pet a ser removido? '))
    for index, animal in enumerate(animais):
        if nome_pet in animal:
            print(f'{color_red} O animal a ser removido é:  \033[0m {animal}')
            animais.remove(animal)
            return

    print("Não tem o nome pet")

# 3
def exibir_todos_os_animais():
    align = "^"
    width = 48
    fill="="
    message0=" Todos animais "
    print(f"|{color_yellow} {message0:{fill}{align}{width}} \033[0m|")

    # headers
    width = 10
    message1 = 'Nome Pet'
    message2 = 'Espécie'
    message3 = 'Idade'
    message4 = 'Peso(kg)'
    message5 = 'Dono'
    print(f'{color_yellow}|{message1:{align}{width}}{message2:{align}{width}}{message3:{align}{width}}{message4:{align}{width}}{message5:{align}{width}}|\033[0m')

    for animal in animais:
        nome_pet = animal[0]
        especie = animal[1]
        idade = animal[2]
        peso = animal[3]
        dono = animal[4]
        print(f'|{nome_pet:{align}{width}}{especie:{align}{width}}{idade:{align}{width}}{peso:{align}{width}}{dono:{align}{width}}|')
    print('\n\n')

# 4
def buscar_animal_pelo_nome():
    nome_pet = input(" => Qual o nome do animal que deseja procurar?  ")
    for animal in animais:
        if nome_pet in animal[0]:
            print(f"{color_yellow} O pet {nome_pet} possui os dados:\033[0m  {animal}\n")
            return

    print("Não encontramos este pet \n")


# 5
def buscar_animais_do_dono():
    nome_dono = input(" => Qual o nome do dono que deseja procurar os animais?  ")

    animais_encontrados = []
    for index, animal in enumerate(animais):
        if  nome_dono in animal[4]:
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
        if nome_pet in animal:
            encontrou_algum_animal = True
            resposta = input(f'O animal é: {animal}, este é o animal que gostaria de atualizar? (Sim ou Não): ')

            if resposta in ["Sim", "sim", "SIM", "S", "s"]:
                nova_especie = str(input('Qual a espécie do seu pet?'))
                nova_idade = int(input('Qual a idade do seu pet?'))
                novo_peso = float(input('Qual o peso do seu pet?'))

                pet_atualizado = [animal[0], nova_especie, nova_idade, novo_peso, animal[4]]

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

    user_input = None
    while True:
        try:
            user_input = input("Como posso ajudar?\n")

            if not user_input.isnumeric() or int(user_input) not in range(7):
                print("Por favor digite uma opção valida!!!\n")
                continue

            if int(user_input) == 0:
                sair()
            if int(user_input) == 1:
                adicionar_animal()
            if int(user_input) == 2:
                remover_animal()
            if int(user_input) == 3:
                exibir_todos_os_animais()
            if int(user_input) == 4:
                buscar_animal_pelo_nome()
            if int(user_input) == 5:
                buscar_animais_do_dono()
            if int(user_input) == 6:
                atualizar_animal()

        except (KeyboardInterrupt, EOFError):
            sair()
        except (KeyError):
            print("Comando não reconhecido. Digite 'help' ou 'ajuda' para listar as ações disponíveis")


if __name__ == "__main__":
    iniciar_loop_principal()
