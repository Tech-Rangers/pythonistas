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

"""
1. Double underscore main (__main__) é sempre o script sendo executado
2. Double underscore name (__name__) refere-se ao nome do modulo.
3. Se o script sendo executado for o próprio módulo,  __name__ é __main__,
portanto protegemos a execução do script dentro do "if main guard"
"""

if __name__ == "__main__":
    print(f"Este é o modulo de dados, nome é {__name__}")
    print(f"Executando scrypt de dados.py")