import json

placar_x = 0
placar_o = 0

vitorias = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def salvar_placar(placar_x, placar_o):

    dados = {
        "Jogador X": placar_x,
        "Jogador O": placar_o
    }

    with open("placar.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def mostrar_placar():

    try:

        with open("placar.json", "r") as arquivo:
            dados = json.load(arquivo)

        print("\n======= PLACAR SALVO =======")
        print("Jogador X:", dados["Jogador X"])
        print("Jogador O:", dados["Jogador O"])
        print("============================")

    except FileNotFoundError:

        print("\nNenhum placar salvo encontrado!")


def mostrar_tabuleiro(tabuleiro):

    print()

    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("--+---+--")

    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("--+---+--")

    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

    print()


def verificar_vitoria(tabuleiro):

    for posicao in vitorias:

        a, b, c = posicao

        if (
            tabuleiro[a] == tabuleiro[b]
            and tabuleiro[b] == tabuleiro[c]
            and tabuleiro[a] in ["X", "O"]
        ):
            return True

    return False


def alerta_perigo(tabuleiro, jogador):

    adversario = "O" if jogador == "X" else "X"

    for posicao in vitorias:

        valores = [
            tabuleiro[posicao[0]],
            tabuleiro[posicao[1]],
            tabuleiro[posicao[2]]
        ]

        if valores.count(adversario) == 2:

            for valor in valores:

                if valor not in ["X", "O"]:

                    print("Cuidado! O adversario pode vencer!")
                    return


while True:

    tabuleiro = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    jogador = "X"
    jogadas = 0
    vencedor = False

    while jogadas < 9:

        print("\n=========== PLACAR ===========")
        print("Jogador X:", placar_x)
        print("Jogador O:", placar_o)
        print("==============================")

        mostrar_tabuleiro(tabuleiro)

        alerta_perigo(tabuleiro, jogador)

        try:

            escolha = int(
                input(f"Jogador {jogador}, escolha uma posicao (1-9): ")
            )

        except ValueError:
            print("Digite apenas numeros!")
            continue

        if escolha < 1 or escolha > 9:
            print("Escolha um numero entre 1 e 9!")
            continue

        if tabuleiro[escolha - 1] in ["X", "O"]:
            print("Essa posicao ja esta ocupada!")
            continue

        tabuleiro[escolha - 1] = jogador

        jogadas += 1

        if verificar_vitoria(tabuleiro):

            mostrar_tabuleiro(tabuleiro)

            print(f"Jogador {jogador} venceu!")

            if jogador == "X":
                placar_x += 1
            else:
                placar_o += 1

            salvar_placar(placar_x, placar_o)

            vencedor = True
            break

        jogador = "O" if jogador == "X" else "X"

    if not vencedor:

        mostrar_tabuleiro(tabuleiro)

        print("Empate!")

        salvar_placar(placar_x, placar_o)

    mostrar_placar()

    jogar_novamente = input(
        "\nDeseja jogar novamente? (s/n): "
    ).lower()

    if jogar_novamente != "s":
        break

print("\nFim do jogo!")
