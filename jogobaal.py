import pygame
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

TITLE = "jogo do satanas"

pontos = 0
PONTOS_PRA_GANHAR = 666
vidas = 3
estado_jogo = "jogando"

heroi = Actor("tohao", (100, 100))
moeda = Actor("moeda", (400, 300))
inimigo = Actor("esiqueleto", (200, 200))

estado_vagabundo = "andando"


raio_de_visao_qd = 100
VELOCIDADE_GUARDA_PERSEGUICAO = 2

rota_patrulha = [
    (200, 200),
    (600, 200),
    (600, 400),
    (200, 400)
]

indice_rota = 0


def draw():

    if estado_jogo == "jogando":

        screen.fill((90, 8, 70))

        heroi.draw()
        moeda.draw()
        inimigo.draw()

        if estado_vagabundo == "PERSEGUISAO":
            cor_visao = (255, 50, 50)
        else:
            cor_visao = (100, 100, 255)

        screen.draw.circle(
            inimigo.pos,
            raio_de_visao_qd,
            cor_visao
        )

        if estado_vagabundo == "PERSEGUISAO":
            status_alert = "FUDEU IRMAO O CARA TE VIU"
        else:
            status_alert = "status: Oculto"

        screen.draw.text(
            status_alert,
            midbottom=(WIDTH // 2, HEIGHT - 15),
            fontsize=22,
            color="crimson"
            if estado_vagabundo == "PERSEGUISAO"
            else "lime"
        )

        screen.draw.text(
            f"pontos: {pontos}/{PONTOS_PRA_GANHAR}",
            topleft=(20, 20),
            fontsize=40,
            color="white",
            shadow=(1, 1),
            scolor="black"
        )

        screen.draw.text(
            f"vidas: {vidas}/3",
            topleft=(20, 65),
            fontsize=30,
            color="white",
            shadow=(1, 1),
            scolor="black"
        )

    elif estado_jogo == "ganhou caralho":

        screen.fill((90, 8, 70))

        screen.draw.text(
            "ganhou filho da puta",
            center=(WIDTH // 2, 220),
            fontsize=64,
            color="green",
            shadow=(1, 1),
            scolor="black"
        )

        screen.draw.text(
            "aperte R para jogar novamente",
            center=(WIDTH // 2, 320),
            fontsize=30,
            color="yellow"
        )

    elif estado_jogo == "morreu porra":

        screen.fill((0, 0, 0))

        screen.draw.text(
            "morreu porra",
            center=(WIDTH // 2, 220),
            fontsize=64,
            color="crimson",
            shadow=(1, 1),
            scolor="black"
        )

        screen.draw.text(
            "aperte R para jogar novamente",
            center=(WIDTH // 2, 320),
            fontsize=30,
            color="yellow"
        )


def update():

    global pontos
    global vidas
    global estado_jogo

    if estado_jogo != "jogando":
        return

    if keyboard.right:
        heroi.x = heroi.x + 5

    if keyboard.left:
        heroi.x = heroi.x - 5

    if keyboard.up:
        heroi.y = heroi.y - 5

    if keyboard.down:
        heroi.y = heroi.y + 5

    if heroi.x < 20:
        heroi.x = 20

    if heroi.x > WIDTH - 20:
        heroi.x = WIDTH - 20

    if heroi.y < 20:
        heroi.y = 20

    if heroi.y > HEIGHT - 20:
        heroi.y = HEIGHT - 20

    if heroi.colliderect(moeda):

        pontos = pontos + 1

        moeda.x = random.randint(50, WIDTH - 50)
        moeda.y = random.randint(50, HEIGHT - 50)

    if pontos >= PONTOS_PRA_GANHAR:
        estado_jogo = "ganhou caralho"
        return

    atualizar_vagabundo()

    if heroi.colliderect(inimigo):

        vidas = vidas - 1

        inimigo.x = random.randint(50, WIDTH - 50)
        inimigo.y = random.randint(50, HEIGHT - 50)

        if vidas <= 0:
            estado_jogo = "morreu porra"


def atualizar_vagabundo():

    global estado_vagabundo
    global indice_rota

    dx = heroi.x - inimigo.x
    dy = heroi.y - inimigo.y

    distancia_qd = dx**2 + dy**2

    if distancia_qd <= raio_de_visao_qd**2:

        estado_vagabundo = "PERSEGUISAO"

    else:

        estado_vagabundo = "andando"

    if estado_vagabundo == "PERSEGUISAO":

        if inimigo.x < heroi.x:
            inimigo.x += VELOCIDADE_GUARDA_PERSEGUICAO

        elif inimigo.x > heroi.x:
            inimigo.x -= VELOCIDADE_GUARDA_PERSEGUICAO

        if inimigo.y < heroi.y:
            inimigo.y += VELOCIDADE_GUARDA_PERSEGUICAO

        elif inimigo.y > heroi.y:
            inimigo.y -= VELOCIDADE_GUARDA_PERSEGUICAO

    else:

        alvo_x, alvo_y = rota_patrulha[indice_rota]

        if inimigo.x < alvo_x:
            inimigo.x += VELOCIDADE_GUARDA_PERSEGUICAO

        elif inimigo.x > alvo_x:
            inimigo.x -= VELOCIDADE_GUARDA_PERSEGUICAO

        if inimigo.y < alvo_y:
            inimigo.y += VELOCIDADE_GUARDA_PERSEGUICAO

        elif inimigo.y > alvo_y:
            inimigo.y -= VELOCIDADE_GUARDA_PERSEGUICAO

        if abs(inimigo.x - alvo_x) < 5 and abs(inimigo.y - alvo_y) < 5:

            indice_rota = (indice_rota + 1) % len(rota_patrulha)


def on_key_down(key):

    global pontos
    global vidas
    global estado_jogo
    global indice_rota
    global estado_vagabundo

    if key == keys.R:

        if estado_jogo == "ganhou caralho" or estado_jogo == "morreu porra":

            pontos = 0
            vidas = 3
            estado_jogo = "jogando"

            heroi.pos = (100, 100)
            moeda.pos = (400, 300)
            inimigo.pos = (200, 200)

            indice_rota = 0
            estado_vagabundo = "andando"


pgzrun.go()
