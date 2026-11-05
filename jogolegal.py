import pygame
import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "jogo do satanas que saiu do inferno pra buscar os malditos que estao proibindo o uso de crar e essa tarde eu vou invocar o baal pra me ajudar a matar o jogo do satanas"

pontos = 0
PONTOS_PRA_GANHAR = 666
vidas = 3
estado_jogo = "jogando"

heroi = Actor("tohao", (100, 100))
moeda = Actor("moeda", (400, 300))
inimigo = Actor("esiqueleto", (200, 200))

estado_vagabundo = "andando"
indice_rota = 0
VELOCIDADE_GUARDA_PERSEGUICAO = 1
raio_de_visao_qd = 150

rota_patrulha = [
    (200, 200),
    (600, 200),
    (600, 400),
    (200, 400)
]


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

        screen.draw.circle(inimigo.pos, 150, cor_visao)

        screen.draw.text(
            f"pontos: {pontos}/{PONTOS_PRA_GANHAR}",
            topleft=(20, 20),
            fontsize=40,
            color="white",
            shadow=(1, 1),
            scolor="black"
        )

    elif estado_jogo == "morreu porra":
        screen.draw.text(
            "morreu porra",
            center=(WIDTH // 2, 220),
            fontsize=64,
            color="green",
            shadow=(1, 1),
            scolor="black"
        )


def update():
    global pontos, vidas, estado_jogo

    if estado_jogo != "jogando":
        return

    if keyboard.right:
        heroi.x += 5

    if keyboard.left:
        heroi.x -= 5

    if keyboard.up:
        heroi.y -= 5

    if keyboard.down:
        heroi.y += 5

    if heroi.colliderect(moeda):
        pontos += 1
        moeda.x = random.randint(50, WIDTH - 50)
        moeda.y = random.randint(50, HEIGHT - 50)

    if heroi.colliderect(inimigo):
        vidas -= 1
        inimigo.x = random.randint(0, WIDTH)
        inimigo.y = random.randint(0, HEIGHT)

    if vidas <= 0:
        estado_jogo = "morreu porra"

    atualizar_vagabundo()


def atualizar_vagabundo():
    global estado_vagabundo, indice_rota

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


pgzrun.go()
