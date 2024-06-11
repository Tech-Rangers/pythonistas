import random #isso era pra gerar números aleatórios

def print_in_red(message: str) -> None:
    print(f'\33[31m{message}')

def print_in_green(message: str) -> None:
    print(f'\33[32m{message}')

def print_in_white(message: str) -> None:
    print(f'\033[0m{message}')

alunos = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isabel", "Jack",
            "Katie", "Liam", "Mia", "Noah", "Olivia", "Patrick", "Quinn", "Rachel", "Sam", "Tina",
            "Ursula", "Victor", "Wendy", "Xander", "Yvonne", "Zack", "Amelia", "Ben", "Catherine", "Daniel",
            "Emma", "Finn", "Gabriella", "Hannah", "Ian", "Jessica", "Kevin", "Lily", "Michael", "Nora"]

notas = [7.3, 4.6, 9.1, 6.2, 3.4, 8.5, 2.7, 5.8, 1.3, 9.9,
          6.5, 7.8, 2.1, 3.6, 4.9, 8.2, 1.0, 9.4, 5.2, 6.7,
          3.8, 7.1, 4.0, 2.5, 8.7, 6.4, 5.1, 9.0, 2.3, 4.8,
          7.9, 3.2, 6.8, 1.7, 8.4, 5.6, 9.2, 2.9, 4.1, 7.0]

fill = " "
align = "<" # ['<', '>', '^']
width = 20

mensagem1 = "Students"
mensagem2 = "Grades"
mensagem3 = "Status"

reprovados = []

print(f"|{mensagem1:{fill}{'^'}{width}} | {mensagem2:{fill}{'^'}{12}} | {mensagem3:{fill}{'^'}{width}}|")

for indice in range(0,40):
    if notas[indice] >= 5:
        status = 'Passed!'
        print_in_green(f"|{alunos[indice]:{fill}{align}{width}} | {notas[indice]:{fill}{align}{12}} | {status:{fill}{align}{width}}|")

    else:
        status = 'Failed!'
        nome_do_aluno_reprovado = alunos[indice]
        reprovados.append(nome_do_aluno_reprovado)
        print_in_red(f"|{alunos[indice]:{fill}{align}{width}} | {notas[indice]:{fill}{align}{12}} | {status:{fill}{align}{width}}|")


  
print_in_white('\n\nLista de alunos reprovados:')

for i in reprovados:
    print(i)

print('\nDone!')
