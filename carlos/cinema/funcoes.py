import random

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


def escolher_filme(filmes):
    return random.choice(filmes)

def comprar_ingresso_solo(salas_passando_filme, pessoa, filme):
    print(f'Compra de ingresso solo: {pessoa}')
    for letra, fileira in enumerate(salas_passando_filme[filme]):
        for numero, assento in enumerate(fileira):
            if assento == 0:
                salas_passando_filme[filme][letra][numero] = 1
                print(f"Filme {filme} - Assento comprado {converter_numero_do_assento(letra, numero)} ")
                return


def comprar_ingresso_casal(salas_passando_filme, casal, filme):
    print(f'Compra de ingresso casal: {casal}')
    for i, fileira in enumerate(salas_passando_filme[filme]):
        for j, assento in enumerate(fileira):
            if j == len(fileira) - 1:
                continue

            assento_lado = fileira [j + 1]

            if assento == 0 and assento_lado == 0:
                salas_passando_filme[filme][i][j] = 1
                salas_passando_filme[filme][i][j + 1] = 1
                print(f"Filme {filme} - Assentos comprados {converter_numero_do_assento(i, j)} e {converter_numero_do_assento(i, j + 1)} ")
                # compras_realizadas.append(casal)
                #print(f"As compras realizadas são: {compras_realizadas} para o filme {filme}")
                return
    print(f"Não foi possivel realizar esta compra para o filme: {filme}")





if __name__ == "__main__":
    print(f"Este é o modulo de funções, nome é {__name__}")
    print(f"Executando scrypt de funcoes.py")