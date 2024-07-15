import random
from cinema import pessoas, filmes, escolher_filme

def dice_roll():
    valor = random.randint(1, 6)
    return valor


if __name__ == "__main__":
    for pessoa in pessoas:
        if type(pessoa) == str:
            valor = dice_roll()
            print(f"{pessoa} jogou o dado e tirou {valor}")
            filme_escolhido = escolher_filme(filmes)
            print(f"{pessoa} escolheu o filme {filme_escolhido}")